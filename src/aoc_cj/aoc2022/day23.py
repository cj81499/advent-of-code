import itertools
from collections import defaultdict, deque
from collections.abc import Iterable
from typing import DefaultDict

import more_itertools as mi

ELF = "#"
EMPTY_GROUND = "."

NORTH = complex(0, -1)
SOUTH = complex(0, 1)
WEST = complex(-1, 0)
EAST = complex(1, 0)


def elf_count(elf_positions: set[complex], to_check: Iterable[complex]) -> int:
    return sum(1 for p in to_check if p in elf_positions)


def parta(txt: str, *, rounds: int = 10) -> int:
    elf_positions = {complex(x, y) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c == ELF}

    check_order = deque("NSWE")
    for round in range(rounds):
        print(f"ROUND {round+1}")
        print(f"check order:", [*check_order])

        # first half
        proposed_moves: DefaultDict[complex, set[complex]] = defaultdict(set)
        # If no other Elves are in one of those eight positions, the Elf does not do anything during this round
        for p in elf_positions:
            nw = p + NORTH + WEST
            n = p + NORTH
            ne = p + NORTH + EAST
            w = p + WEST
            e = p + EAST
            sw = p + SOUTH + WEST
            s = p + SOUTH
            se = p + SOUTH + EAST

            # If no other Elves are in one of those eight positions, the Elf does not do anything during this round.
            if elf_count(elf_positions, (nw, n, ne, w, e, sw, s, se)) == 0:
                continue

            CHECKS = {
                "N": (n, ne, nw),
                "S": (s, se, sw),
                "W": (w, nw, sw),
                "E": (e, ne, se),
            }

            for c in check_order:
                check = CHECKS[c]
                if elf_count(elf_positions, check) == 0:
                    proposed_moves[check[0]].add(p)
                    break
        # second half
        # print(proposed_moves)
        accepted_moves = {mi.only(srcs): dest for dest, srcs in proposed_moves.items() if len(srcs) == 1}
        # print(accepted_moves)
        # print()

        # print("BEFORE")
        # print(elf_positions)
        for src, dest in accepted_moves.items():
            assert src is not None
            elf_positions.remove(src)
            elf_positions.add(dest)
        # print()
        # print("AFTER")
        # print(elf_positions)
        print(f"END OF ROUND {round+1}")
        for y in range(-2, 10):
            for x in range(-3, 11):
                print(ELF if complex(x, y) in elf_positions else EMPTY_GROUND, end="")
            print()
        # print(elf_positions)
        print()
        check_order.rotate(-1)

    min_x = min(int(p.real) for p in elf_positions)
    max_x = max(int(p.real) for p in elf_positions)
    min_y = min(int(p.imag) for p in elf_positions)
    max_y = max(int(p.imag) for p in elf_positions)

    dx = max_x - min_x + 1
    dy = max_y - min_y + 1
    area = dx * dy

    print(f"{area=}, {dx=}, {dy=}, {min_x=}, {max_x=}, {min_y=}, {max_y=}")
    print(elf_positions)
    return area - len(elf_positions)


def partb(txt: str) -> int:
    elf_positions = {complex(x, y) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c == ELF}

    check_order = deque("NSWE")
    for round in itertools.count(start=1):
        # first half
        proposed_moves: DefaultDict[complex, set[complex]] = defaultdict(set)
        # If no other Elves are in one of those eight positions, the Elf does not do anything during this round
        for p in elf_positions:
            nw = p + NORTH + WEST
            n = p + NORTH
            ne = p + NORTH + EAST
            w = p + WEST
            e = p + EAST
            sw = p + SOUTH + WEST
            s = p + SOUTH
            se = p + SOUTH + EAST

            # If no other Elves are in one of those eight positions, the Elf does not do anything during this round.
            if elf_count(elf_positions, (nw, n, ne, w, e, sw, s, se)) == 0:
                continue

            CHECKS = {
                "N": (n, ne, nw),
                "S": (s, se, sw),
                "W": (w, nw, sw),
                "E": (e, ne, se),
            }

            for c in check_order:
                check = CHECKS[c]
                if elf_count(elf_positions, check) == 0:
                    proposed_moves[check[0]].add(p)
                    break
        # second half
        accepted_moves = {mi.only(srcs): dest for dest, srcs in proposed_moves.items() if len(srcs) == 1}

        if len(accepted_moves) == 0:
            return round

        for src, dest in accepted_moves.items():
            assert src is not None
            elf_positions.remove(src)
            elf_positions.add(dest)

        check_order.rotate(-1)

    min_x = min(int(p.real) for p in elf_positions)
    max_x = max(int(p.real) for p in elf_positions)
    min_y = min(int(p.imag) for p in elf_positions)
    max_y = max(int(p.imag) for p in elf_positions)

    dx = max_x - min_x + 1
    dy = max_y - min_y + 1
    area = dx * dy

    print(f"{area=}, {dx=}, {dy=}, {min_x=}, {max_x=}, {min_y=}, {max_y=}")
    print(elf_positions)
    return area - len(elf_positions)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
