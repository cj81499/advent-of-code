from __future__ import annotations

from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def parta(txt: str):
    p = IntcodeProgram.parse(txt)
    p.run()
    video_feed = "".join(chr(c) for c in p.outputs)
    return sum_of_alignment_parameters(video_feed)


def sum_of_alignment_parameters(video_feed):
    s = scaffolding(video_feed)
    intersections = {(x, y) for (x, y) in s if all(a in s for a in adj(x, y))}
    return sum(x * y for x, y in intersections)


def positions(video_feed, chars):
    yield from ((x, y) for y, row in enumerate(video_feed.splitlines()) for x, c in enumerate(row) if c in chars)


def scaffolding(video_feed):
    return set(positions(video_feed, set("#")))


def adj(x, y):
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y


def full_route(video_feed):
    DIRECTIONS = {"^": +0 - 1j, ">": +1 + 0j, "v": +0 + 1j, "<": -1 + 0j}
    video_feed = {complex(x, y): c for y, row in enumerate(video_feed.splitlines()) for x, c in enumerate(row)}
    pos = next((p, DIRECTIONS[c]) for p, c in video_feed.items() if c in set("^v<>"))
    route = []
    can_move = True
    while can_move:
        # check if we can move forwards
        p, d = pos
        left = complex(d.imag, -d.real)
        right = complex(-d.imag, d.real)
        forward_move = p + d
        left_move = p + left
        right_move = p + right
        if video_feed.get(forward_move, ".") == "#":
            if isinstance(route[-1], int):
                route[-1] += 1
            else:
                route.append(1)
            pos = (forward_move, d)
        elif video_feed.get(left_move, ".") == "#":
            route.append("L")
            pos = (p, left)
        elif video_feed.get(right_move, ".") == "#":
            route.append("R")
            pos = (p, right)
        else:
            can_move = False
    return ",".join(map(str, route))


def generate_main_routine(full, a, b, c):
    full = "".join(full)
    a = "".join(a)
    b = "".join(b)
    c = "".join(c)
    main_routine = []
    i = 0
    while i < len(full):
        if full[i:].startswith(a):
            i += len(a)
            main_routine.append("A")
        elif full[i:].startswith(b):
            i += len(b)
            main_routine.append("B")
        elif full[i:].startswith(c):
            i += len(c)
            main_routine.append("C")
        else:
            return None
        if len(main_routine) > 20:
            return None
    return main_routine


def plan_route(full):
    full = full.split(",")
    for i1 in range(len(full)):
        for j1 in range(i1 + 1, min(i1 + 21, len(full))):
            for i2 in range(j1, min(j1 + 21, len(full))):
                for j2 in range(i2 + 1, min(i2 + 21, len(full))):
                    for i3 in range(j2, min(j2 + 21, len(full))):
                        for j3 in range(i3 + 1, min(i3 + 21, len(full))):
                            a = full[i1:j1]
                            b = full[i2:j2]
                            c = full[i3:j3]
                            main_r = generate_main_routine(full, a, b, c)
                            if main_r is not None:
                                return [main_r, a, b, c]


def partb(txt: str):
    p = IntcodeProgram.parse(txt)
    assert p[0] == 1
    p[0] = 2  # wake up the robot
    p.run()

    # get the initial video feed
    video_feed, _main_prompt = "".join(chr(c) for c in p.outputs).split("\n\n")

    # plan the route
    full = full_route(video_feed)
    plan = [",".join(x) for x in plan_route(full)]

    # input the plan
    for f in plan:
        for x in f:
            p.write_input(ord(x))
        p.write_input(ord("\n"))

    # # for continuous output (while testing)
    # p.write_input(ord("y"))
    # p.write_input(ord("\n"))
    # leftover = ""
    # while not p.terminated:
    #     try:
    #         p.run(max_steps=100)
    #     except:
    #         pass

    #     if len(p.outputs) > 0:
    #         if p.outputs[-1] in range(0x110000):
    #             leftover += "".join(chr(x) for x in p.outputs)
    #         else:
    #             leftover += "".join(chr(x) for x in [*p.outputs][:-1])
    #         # if we have one or more full screens
    #         if "\n\n" in leftover:
    #             chunks = leftover.split("\n\n")
    #             # print each full screen
    #             for c in chunks[:-1]:
    #                 print(c)
    #                 print()
    #             # and set leftover to whatever we didn't print
    #             leftover = chunks[-1]
    #         if p.outputs[-1] not in range(0x110000):
    #             return p.outputs[-1]
    #         p.outputs.clear()

    # no to continuous output
    p.write_input(ord("n"))
    p.write_input(ord("\n"))

    # execute
    p.run()
    return p.outputs[-1]


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
