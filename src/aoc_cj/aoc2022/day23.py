from collections import defaultdict, deque
from collections.abc import Iterable
from typing import Literal

CardinalDirection = Literal["N", "W", "E", "S"]
Direction = Literal[CardinalDirection, "NW", "NE", "SW", "SE"]

NORTH = complex(0, -1)
SOUTH = complex(0, 1)
WEST = complex(-1, 0)
EAST = complex(1, 0)


def adj(p: complex) -> dict[Direction, complex]:
    return {
        "NW": p + NORTH + WEST,
        "N": p + NORTH,
        "NE": p + NORTH + EAST,
        "W": p + WEST,
        "E": p + EAST,
        "SW": p + SOUTH + WEST,
        "S": p + SOUTH,
        "SE": p + SOUTH + EAST,
    }


class Simulation:
    def __init__(self, elf_positions: set[complex]) -> None:
        self._elves = elf_positions
        self.is_complete = False
        self.round = 0
        self._check_order = deque[CardinalDirection](("N", "S", "W", "E"))

    def simulate_round(self) -> None:
        assert not self.is_complete, "simulation is already complete"
        self.round += 1

        proposed_moves = self._get_proposed_moves()  # first half of round
        self._move_elves(proposed_moves)  # second half of round

    def _get_proposed_moves(self) -> defaultdict[complex, set[complex]]:
        # map position to position of elves that want to move there
        proposed_moves = defaultdict[complex, set[complex]](set)

        for elf_pos in self._elves:
            adjacent = adj(elf_pos)

            # if there are no adjacent elves, the elf does nothing
            if not self.any_elf(adjacent.values()):
                continue

            for check_direction in self._check_order:
                # if none of the spaces to the `check_direction` of are elves, an elf proposes a move in that direction
                if not self.any_elf(adj_p for direction, adj_p in adjacent.items() if check_direction in direction):
                    proposed_moves[adjacent[check_direction]].add(elf_pos)
                    break  # an elf can only propose 1 move per turn

        return proposed_moves

    def _move_elves(self, proposed_moves: dict[complex, set[complex]]) -> None:
        accepted_moves = {srcs.pop(): dest for dest, srcs in proposed_moves.items() if len(srcs) == 1}

        if len(accepted_moves) == 0:
            self.is_complete = True
            return

        # move the elves
        self._elves.difference_update(accepted_moves)  # remove the old positions
        self._elves.update(accepted_moves.values())  # add the new positions

        self._check_order.rotate(-1)

    def covered_ground(self) -> int:
        min_x = min(int(p.real) for p in self._elves)
        max_x = max(int(p.real) for p in self._elves)
        min_y = min(int(p.imag) for p in self._elves)
        max_y = max(int(p.imag) for p in self._elves)

        dx = max_x - min_x + 1
        dy = max_y - min_y + 1

        area = dx * dy

        return area - len(self._elves)

    @staticmethod
    def parse(initial_state: str) -> "Simulation":
        elf_positions = {
            complex(x, y) for y, line in enumerate(initial_state.splitlines()) for x, c in enumerate(line) if c == "#"
        }
        return Simulation(elf_positions)

    def any_elf(self, to_check: Iterable[complex]) -> bool:
        return any(p in self._elves for p in to_check)


def part_1(txt: str) -> int:
    s = Simulation.parse(txt)
    for _round in range(10):
        s.simulate_round()
    return s.covered_ground()


def part_2(txt: str) -> int:
    s = Simulation.parse(txt)
    while not s.is_complete:
        s.simulate_round()
    return s.round


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
