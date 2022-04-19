import contextlib
import io
import os
import sys
import unittest
from unittest import TestCase, mock

sys.modules["assess"] = sys.modules[__name__]
dirname = os.path.dirname(__file__)


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


@contextlib.contextmanager
def trace(t):
    try:
        if t:
            t.start()
        yield
    finally:
        if t:
            t.stop()


def runcaptured(tracing=None, variables=None):
    filename = "exercise.py"
    with open(filename) as f:
        source = f.read()
        c = compile(source, filename, "exec")
        with capture() as out, trace(tracing):
            if variables is None:
                variables = {}
            exec(c, variables)
        return source, out[0], out[1], variables


class RefernceSolution:
    def search_itunes(self, search_term):
        import requests

        r = requests.get(
            f"https://itunes.apple.com/search?term={search_term}&entity=album"
        )
        result_json = r.json()

        result_count = result_json["resultCount"]
        albums = [
            (result["artistName"], result["collectionName"], result["trackCount"])
            for result in result_json["results"]
        ]

        return result_count, albums


class Testing(TestCase):
    @mock.patch("builtins.input", create=True)
    def test_search_gold(self, mocked_input):

        result_count, albums = RefernceSolution().search_itunes("gold")

        mocked_input.side_effect = ["gold"]
        self.code, self.std_out, self.error_out, _ = runcaptured()
        output = self.std_out.getvalue().strip()
        lines = output.split("\n")

        self.assertIn(
            str(result_count),
            lines[0],
            f"The first line of the output should contain the number of search results. For the search term 'gold' this should {result_count}.",
        )

        for album in albums:
            self.assertIn(
                album[0],
                output,
                f"For the search term 'gold' the result should contain the artist {album[0]}",
            )
            self.assertIn(
                album[1],
                output,
                f"For the search term 'gold' the result should contain the album {album[1]}",
            )
            self.assertIn(
                str(album[2]),
                output,
                f"For the search term 'gold' the result should contain the track count {album[2]}",
            )


if __name__ == "__main__":
    unittest.main()
