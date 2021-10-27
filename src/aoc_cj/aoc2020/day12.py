NORTH = (0, -1)
SOUTH = (0, 1)
WEST = (-1, 0)
EAST = (1, 0)

DIRECTIONS = {"N": NORTH, "S": SOUTH, "W": WEST, "E": EAST}


def add_pos(pos_a, pos_b, multiplier=1):
    return (pos_a[0] + multiplier * pos_b[0], pos_a[1] + multiplier * pos_b[1])


def turn_left(pos):
    return (pos[1], -pos[0])


def turn_right(pos):
    return (-pos[1], pos[0])


def turn_around(pos):
    return (-pos[0], -pos[1])


def handle_turn(pos, action, angle):
    if angle == 180:
        return turn_around(pos)
    turns = (turn_left, turn_right)
    if action == "R":
        turns = tuple(reversed(turns))
    return (turns[0] if angle == 90 else turns[1])(pos)


def parta(txt):
    pos = (0, 0)
    heading = EAST
    for instruction in txt.splitlines():
        action, *n = instruction
        n = int("".join(n))
        if action in "NSWE":
            pos = add_pos(pos, DIRECTIONS[action], n)
        elif action in "LR":
            heading = handle_turn(heading, action, n)
        elif action == "F":
            pos = add_pos(pos, heading, n)
    return sum(abs(x) for x in pos)


def partb(txt):
    pos = (0, 0)
    waypoint = (10, -1)
    for instruction in txt.splitlines():
        action, *n = instruction
        n = int("".join(n))
        if action in "NSWE":
            waypoint = add_pos(waypoint, DIRECTIONS[action], n)
        elif action in "LR":
            waypoint = handle_turn(waypoint, action, n)
        elif action == "F":
            pos = add_pos(pos, waypoint, n)
    return sum(abs(x) for x in pos)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
