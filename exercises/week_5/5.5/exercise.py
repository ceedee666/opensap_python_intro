def reaction_path(speed):
    path = speed * 3 / 10
    return path

def brake_distance(speed):
    path = (speed / 10) ** 2
    return path

def stopping_distance(speed):
    path = reaction_path(speed) + brake_distance(speed)
    return path

speed = int(input("What is your speed: "))
path = stopping_distance(speed)

print(path)