import itertools
import re
from collections import deque

from aoc_cj.aoc2019.intcode_computer import IntcodeProgram

r = re.compile(
    r"== (?P<location>.*) ==\n(?P<description>.*)\n\nDoors here lead:\n(?P<doors>(?:- .*\n)+)\n(?:Items here:\n(?P<items>(?:- .*\n)+)\n)?Command\?"
)


def send_cmd(p: IntcodeProgram, cmd: str | None):
    if cmd is not None:
        for c in cmd:
            p.write_input(ord(c))
        p.write_input(ord("\n"))
    p.run()
    output = "".join(chr(c) for c in p.outputs)
    last_output = output.split("\n\n\n")[-1]
    return last_output.strip()


def take(p: IntcodeProgram, item: str):
    return send_cmd(p, f"take {item}")


def drop(p: IntcodeProgram, item: str):
    return send_cmd(p, f"drop {item}")


def get_inventory(p: IntcodeProgram):
    inv = send_cmd(p, "inv").split("\n\n")[-2]
    return {i.lstrip("- ") for i in inv.splitlines()[1:]}


OPPOSITE_DIRECTION = {
    "north": "south",
    "east": "west",
    "south": "north",
    "west": "east",
}

DANGEROUS_ITEMS = {"escape pod", "molten lava", "photons", "infinite loop", "giant electromagnet"}


def handle_move(p: IntcodeProgram, direction: str | None, ship_map: dict, prev_location: str | None):
    output = send_cmd(p, direction)
    match = r.match(output)
    d = match.groupdict()

    # if we haven't seen this location before, add it to the ship map
    if (location := d.get("location")) not in ship_map:
        doors = d.get("doors")
        d["doors"] = {i.lstrip("- "): None for i in doors.splitlines()}
        ship_map[location] = d

    # update the ship map
    if prev_location is not None:
        get_doors(ship_map, prev_location)[direction] = location

    # take all available items, unless it's dangerous
    if (items := d.get("items")) is not None:
        for item in (i.lstrip("- ") for i in items.splitlines()):
            if item not in DANGEROUS_ITEMS:
                take(p, item)

    return location


def explore(p: IntcodeProgram, ship_map, location):
    doors = get_doors(ship_map, location)
    for direction in doors:
        if doors[direction] is None:
            new_location = handle_move(p, direction, ship_map, location)
            explore(p, ship_map, new_location)
            # make sure next loop starts where this loop started (return to original location)
            handle_move(p, OPPOSITE_DIRECTION[direction], ship_map, new_location)


def pathfind(start: str, end: str, ship_map):
    q = deque()
    q.append((start, None, None))
    moves = {}
    while len(q) > 0:
        location, direction, came_from = q.popleft()
        if location not in moves:
            moves[location] = (direction, came_from)
            q.extend((destination, door, location) for door, destination in get_doors(ship_map, location).items())
    path = [(None, end)]
    while path[-1][1] in moves:
        path.append(moves[path[-1][1]])
    return [p[0] for p in reversed(path) if p[0] is not None]


def get_doors(ship_map, location):
    return ship_map[location]["doors"]


def part_1(txt: str):
    p = IntcodeProgram.parse(txt)

    ship_map = {}
    location = handle_move(p, None, ship_map, None)

    explore(p, ship_map, location)

    # move to the security checkpoint
    TARGET_ROOM = "Security Checkpoint"
    path_to_checkpoint = pathfind(location, TARGET_ROOM, ship_map)
    for direction in path_to_checkpoint:
        location = handle_move(p, direction, ship_map, location)

    # direction to move once in security checkpoint
    direction = next(d for d, l in get_doors(ship_map, location).items() if l == TARGET_ROOM)

    # get past the security checkpoint
    all_items = get_inventory(p)
    for size in range(len(all_items)):
        for perm in itertools.combinations(all_items, r=size):
            # get the right items
            perm = set(perm)
            inv = get_inventory(p)
            to_drop = inv - perm
            to_take = perm - inv
            for item in to_drop:
                drop(p, item)
            for item in to_take:
                take(p, item)
            # try to enter
            result = send_cmd(p, direction)
            # if we're in a new location, it worked!
            if not result.startswith(f"== {TARGET_ROOM} =="):
                return next(int(x) for x in result.split() if x.isnumeric())


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
