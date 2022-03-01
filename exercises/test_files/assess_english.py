exercise = __name__[1:]

import contextlib, io, sys, turtle, ast, os, unittest, math

sys.modules["assess"] = sys.modules[__name__]
dirname = os.path.dirname(__file__)

turtle_operations = []
screen_operations = []
bindings = {}
turtles = []


class RecordingPen:
    _pen = None
    _screen = None

    def __init__(self):
        self.operations = turtle_operations
        self._pos = (0, 0)
        self._dir = 0
        self._screen = FakeCanvas(turtle.WebCanvas(FakeShell()))
        turtles.append(self)
        turtle_operations.append(("__init__", ()))

    def reset(self):
        turtle_operations.clear()
        screen_operations.clear()

    def onclick(self, fun, btn=1, add=None):
        self.operations.append(("onclick", (fun,)))

        def eventfun(event):
            fun(event.x, event.y)

        bindings["<Button-1>"] = eventfun

    onscreenclick = onclick

    def goto(self, point_or_x, y=None):
        if isinstance(point_or_x, tuple):
            self._pos = point_or_x
        else:
            self._pos = (point_or_x, y)
        self.operations.append(("goto", self._pos))

    setpos = goto
    setposition = goto

    def left(self, deg):
        self._dir = (self._dir + deg) % 360
        self.operations.append(("left", deg))

    lt = left

    def right(self, deg):
        self._dir = (self._dir - deg) % 360
        self.operations.append(("right", deg))

    rt = right

    def setheading(self, direction):
        self._dir = direction % 360
        self.operations.append(("setheading", direction))

    seth = setheading

    def heading(self):
        self.operations.append(("heading", ()))
        return self._dir

    def forward(self, steps):
        # Canvas precision within turtle is with two digits after the decimal point.
        # Hence, we do the same here as well.
        x = round(self._pos[0] + math.cos(math.radians(self._dir)) * steps, 2)
        y = round(self._pos[1] + math.sin(math.radians(self._dir)) * steps, 2)
        self._pos = (x, y)
        self.operations.append(("forward", steps))

    fd = forward

    def backward(self, steps):
        # Canvas precision within turtle is with two digits after the decimal point.
        # Hence, we do the same here as well.
        x = round(self._pos[0] - math.cos(math.radians(self._dir)) * steps, 2)
        y = round(self._pos[1] - math.sin(math.radians(self._dir)) * steps, 2)
        self._pos = (x, y)
        self.operations.append(("backward", steps))

    bk = backward
    back = backward

    def pos(self):
        # Be sure to check all turtles (using the `turtles` array)
        # if checking for position in test. Otherwise, only the default turtle and
        # no new turtles with `t = Turtle()` will be checked.
        self.operations.append(("pos", ()))
        return self._pos

    position = pos

    def xcor(self):
        self.operations.append(("xcor", ()))
        return self.pos()[0]

    def ycor(self):
        self.operations.append(("ycor", ()))
        return self.pos()[1]

    def setx(self, x):
        self._pos = (x, self.pos()[1])
        self.operations.append(("setx", (x)))

    def sety(self, y):
        self._pos = (self.pos()[0], y)
        self.operations.append(("sety", (y)))

    def distance(self, point_or_x, y=None):
        if isinstance(point_or_x, RecordingPen):
            # point_or_x is another object
            pos = point_or_x.position()
        elif isinstance(point_or_x, tuple):
            # point_or_x is a point: (x, y)
            pos = point_or_x
        elif y is None:
            # y is not set, use same as turtle
            pos = (point_or_x, self._pos[1])
        else:
            # x and y are both numbers (hopefully...)
            pos = (point_or_x, y)
        self.operations.append(("distance", pos))

        return math.sqrt(
            math.pow(pos[0] - self._pos[0], 2) + math.pow(pos[1] - self._pos[1], 2)
        )

    def _screen(self):
        return FakeCanvas(turtle.WebCanvas(FakeShell()))

    def __getattr__(self, method):
        def func(*args):
            self.operations.append((method, args))

        return func


class FakeCanvas(turtle.WebCanvas):
    operations = screen_operations

    def flushbatch(self):
        pass

    def get_width(self):
        return 400

    def get_height(self):
        return 400

    def delete(self, item):
        pass

    def css(self, key, value):
        pass

    def bgcolor(self, color):
        self.operations.append(("bgcolor", color))


class FakeShell:
    def sendpickle(self, data):
        pass

    def receivemsg(self):
        return {"cmd": "result", "exception": "", "result": {"cmd": "result"}}


fake_events = []


def mainloop():
    while fake_events:
        e = turtle.Event(fake_events.pop(0))
        if e.type in bindings:
            bindings[e.type](e)


done = mainloop

turtle.Turtle = RecordingPen
turtle.WebCanvas = FakeCanvas
turtle.Turtle._screen = FakeCanvas(turtle.WebCanvas(FakeShell()))
pen = turtle._getpen()
screen = turtle.Turtle._screen
turtle.mainloop = mainloop


def filter_operations(name):
    return [o for o in turtle_operations if o[0] == name]


@contextlib.contextmanager
def capture():
    global captured_out
    import sys

    oldout, olderr = sys.stdout, sys.stderr
    try:
        out = [io.StringIO(), io.StringIO()]
        captured_out = out
        sys.stdout, sys.stderr = out
        yield out
    finally:
        sys.stdout, sys.stderr = oldout, olderr
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()


def get_source():
    with open("%s/exercise%s.py" % (dirname, exercise)) as f:
        return f.read()


def get_ast(src=get_source()):
    return ast.parse(src, "exercise%s.py" % src, "exec")


def get_src_without_comments(src=get_source()):
    tree = get_ast(src)
    noc = []  # noc: no outer comments (at script level)
    for b in tree.body:
        code = ast.get_source_segment(src, b)  # Since python 3.8
        if code.strip().startswith('"'):
            continue  # remove multiline comments
        if code.strip().startswith("'"):
            continue
        noc.append(code)
    # remove # comments from indented code (kept by ast.parse):
    out = []
    for line in "\n".join(noc).splitlines():
        if not line.strip().startswith("#"):
            out.append(line)
    out = "\n".join(out)  # list to charstring
    return out


def has_bare_except():
    for node in ast.walk(get_ast()):
        if isinstance(node, ast.ExceptHandler):
            if node.type is None:
                return True
    return False


def runcaptured(data=None, tracing=None, variables=None):
    filename = "%s/exercise%s.py" % (dirname, exercise)
    """if data:
        # ToDo: Check that another file called daten.py exists.
        import daten
        daten.__dict__.update(data)"""
    with open(filename) as f:
        source = f.read()
        c = compile(source, filename, "exec")
        with capture() as out, trace(tracing):
            if variables is None:
                variables = {}
            exec(c, variables)
        return source, out[0], out[1], variables


def runfunc(func, *args, tracing=None):
    with capture() as out, trace(tracing):
        res = func(*args)
    return out[0], out[1], res


def passed():
    pass


def failed(msg):
    raise AssertionError(msg)


def modified(variables, name, val):
    if variables.get(name) != val:
        failed("Please do not overwrite the variable %s." % name)
        return True
    return False


undefined = object()


def getvar(variables, name):
    try:
        return variables["name"]
    except KeyError:
        name = name.lower()
        for k, v in variables.items():
            if k.lower() == name:
                return v
        return undefined


def _match(n1, n2, ignoreNone=False):
    if n1 == n2:
        return True
    if n1 is None or n2 is None:
        return ignoreNone
    return n1.lower() == n2.lower()


class Call:
    def __init__(self, name, args):
        self.name = name
        self.args = args
        self.calls = []
        self.current = None

    def findcall(self, f):
        if _match(self.name, f):
            return self
        for c in self.calls:
            r = c.findcall(f)
            if r:
                return r
        return None

    def calling(self, caller, callee):
        if _match(self.name, caller):
            for c in self.calls:
                if _match(c.name, callee):
                    return True
        for c in self.calls:
            if c.calling(caller, callee):
                return True
        return False

    def countcalls(self, caller, callee):
        # Call how often a method call is used.
        # If `caller` is provided (!= None), occurrences only within this method are counted.
        # Otherwise, the whole program execution incl. loops is considered
        calls = 0
        if _match(self.name, caller, caller is None):
            for c in self.calls:
                if _match(c.name, callee):
                    calls += 1
        for c in self.calls:
            r = c.countcalls(caller, callee)
            if r > 0 and caller is not None:
                return r
            calls += r
        return calls


class Tracing(Call):
    def __init__(self):
        Call.__init__(self, None, None)

    def trace(self, frame, event, arg):
        if event == "call":
            c = Call(frame.f_code.co_name, frame.f_locals.copy())
            cur = self
            while cur.current:
                cur = cur.current
            cur.calls.append(c)
            cur.current = c
            return self.trace
        elif event in ("return", "exception"):
            cur = self
            if not cur.current:
                # XXX return without call? happens when invocation of top function fails
                return
            while cur.current.current:
                cur = cur.current
            cur.current = None

    def start(self):
        sys.settrace(self.trace)

    def stop(self):
        sys.settrace(None)


@contextlib.contextmanager
def trace(t):
    try:
        if t:
            t.start()
        yield
    finally:
        if t:
            t.stop()


class Assess(unittest.TestCase):
    def test_assess(self):
        with open("%s/a%s.py" % (dirname, exercise)) as f:
            code = compile(f.read(), "a%s.py" % exercise, "exec")
            try:
                exec(code, globals())
            except AssertionError as e:
                if isinstance(e.__context__, AssertionError):
                    raise e.__context__ from None
                else:
                    raise e from None
