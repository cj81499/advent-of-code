import dataclasses
import enum
import itertools
from collections.abc import Generator, Mapping
from typing import Self, assert_never, override

import more_itertools as mi


class Kind(enum.StrEnum):
    ROBOT = "@"
    WALL = "#"
    BOX = "O"
    BOX_LEFT = "["
    BOX_RIGHT = "]"


class Direction(enum.StrEnum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

    def as_complex(self) -> complex:
        match self:
            case Direction.UP:
                return -1j
            case Direction.DOWN:
                return +1j
            case Direction.LEFT:
                return -1
            case Direction.RIGHT:
                return +1
            case _:
                assert_never(self)


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Grid:
    robot_pos: complex
    grid: Mapping[complex, Kind]

    def move(self, direction: Direction) -> Self:
        cls = type(self)

        delta = direction.as_complex()
        new_robot_pos = self.robot_pos + delta
        val = self.grid.get(new_robot_pos)
        match val:
            case None:
                return cls(robot_pos=new_robot_pos, grid=self.grid)
            case Kind.ROBOT:
                msg = f"Robot found at multiple locations: {self.robot_pos}, {new_robot_pos}."
                raise AssertionError(msg)
            case Kind.WALL:
                return self
            case Kind.BOX:
                positions_in_front_of_robot = (self.robot_pos + delta * i for i in itertools.count(start=1))
                final_box = mi.last(
                    itertools.takewhile(lambda p: self.grid.get(p) is Kind.BOX, positions_in_front_of_robot)
                )
                new_box_pos = final_box + delta
                if self.grid.get(new_box_pos) is Kind.WALL:
                    return self

                # advance box(es)
                new_grid = {p: v for p, v in self.grid.items()}
                assert new_grid.pop(new_robot_pos) == Kind.BOX
                new_grid[new_box_pos] = Kind.BOX
                return cls(robot_pos=new_robot_pos, grid=new_grid)
            case Kind.BOX_LEFT | Kind.BOX_RIGHT:
                to_advance: list[complex] = []
                to_check = {new_robot_pos}
                while to_check:
                    checking_pos = to_check.pop()
                    checking_val = self.grid.get(checking_pos)
                    match checking_val:
                        case None:
                            pass
                        case Kind.ROBOT:
                            msg = f"Robot movement handled specially"
                            raise AssertionError(msg)
                        case Kind.BOX:
                            msg = f"BOX (not left or right) found while solving part 2"
                            raise AssertionError(msg)
                        case Kind.WALL:
                            return self
                        case Kind.BOX_LEFT | Kind.BOX_RIGHT:
                            other_half_pos = checking_pos + (1 if checking_val is Kind.BOX_LEFT else -1)
                            other_half_kind = Kind.BOX_RIGHT if checking_val is Kind.BOX_LEFT else Kind.BOX_LEFT
                            assert self.grid.get(other_half_pos) == other_half_kind

                            # handle whatever's in front of either side
                            if (p := checking_pos + delta) not in (checking_pos, other_half_pos):
                                to_check.add(p)
                            if (p := other_half_pos + delta) not in (checking_pos, other_half_pos):
                                to_check.add(p)

                            to_advance.append(checking_pos)
                            to_advance.append(other_half_pos)
                        case _:
                            assert_never(checking_val)
                new_grid = {p: v for p, v in self.grid.items() if p not in to_advance}
                for p in to_advance:
                    new_grid[p + delta] = self.grid[p]
                return cls(robot_pos=new_robot_pos, grid=new_grid)
            case _:
                assert_never(val)

    @override
    def __str__(self) -> str:
        max_x = max(int(p.real) for p in self.grid)
        max_y = max(int(p.imag) for p in self.grid)
        return "\n".join(
            "".join(
                self.grid.get((p := x + y * 1j), Kind.ROBOT if p == self.robot_pos else ".") for x in range(max_x + 1)
            )
            for y in range(max_y + 1)
        )

    def gps_score(self) -> int:
        return sum(100 * int(p.imag) + int(p.real) for p, k in self.grid.items() if k in (Kind.BOX, Kind.BOX_LEFT))


def part_1(txt: str) -> int:
    return solve(txt)


def part_2(txt: str) -> int:
    return solve(txt, double_width=True)


def solve(txt: str, *, double_width: bool = False) -> int:
    moves, grid = parse(txt, double_width=double_width)
    for m in moves:
        grid = grid.move(m)
    return grid.gps_score()


def parse(txt: str, *, double_width: bool = False) -> tuple[Generator[Direction, None, None], Grid]:
    initial_state, moves = txt.split("\n\n")
    state = (
        initial_state.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")
        if double_width
        else initial_state
    )
    grid = {x + y * 1j: Kind(c) for y, row in enumerate(state.splitlines()) for x, c in enumerate(row) if c != "."}

    robot_pos = mi.one(p for p, k in grid.items() if k is Kind.ROBOT)
    assert grid.pop(robot_pos) is Kind.ROBOT

    return (Direction(m) for m in moves if m != "\n"), Grid(robot_pos=robot_pos, grid=grid)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
