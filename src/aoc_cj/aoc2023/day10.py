import abc
import dataclasses
import enum
from collections.abc import Iterable
from typing import Final, assert_never, override

import frozendict
import more_itertools as mi

from aoc_cj import util


class ComplexEnum(complex, enum.ReprEnum):
    """
    Enum where members are also (and must be) `complex`s
    """


class Direction(ComplexEnum):
    NORTH = -1j
    SOUTH = 1j
    WEST = -1
    EAST = 1


ANIMAL: Final = "S"


class Pipe(enum.StrEnum):
    NORTH_SOUTH = "|"
    EAST_WEST = "-"
    NORTH_EAST = "L"
    NORTH_WEST = "J"
    SOUTH_WEST = "7"
    SOUTH_EAST = "F"

    def connected_directions(self) -> tuple[Direction, Direction]:
        match self:
            case Pipe.NORTH_SOUTH:
                return Direction.NORTH, Direction.SOUTH
            case Pipe.EAST_WEST:
                return Direction.EAST, Direction.WEST
            case Pipe.NORTH_EAST:
                return Direction.NORTH, Direction.EAST
            case Pipe.NORTH_WEST:
                return Direction.NORTH, Direction.WEST
            case Pipe.SOUTH_WEST:
                return Direction.SOUTH, Direction.WEST
            case Pipe.SOUTH_EAST:
                return Direction.SOUTH, Direction.EAST
        assert_never(self)


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class GridEntry(abc.ABC):
    pos: complex
    grid: Grid

    @abc.abstractmethod
    def connections(self) -> Iterable[GridEntry]: ...


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class AnimalGridEntry(GridEntry):
    @override
    def connections(self) -> Iterable[GridEntry]:
        return (ge for p in util.adj_4(self.pos) if (ge := self.grid.get(p)) is not None and self in ge.connections())


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class PipeGridEntry(GridEntry):
    pipe: Pipe

    @override
    def connections(self) -> Iterable[GridEntry]:
        return (ge for d in self.pipe.connected_directions() if (ge := self.grid.get(self.pos + d)) is not None)


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Grid:
    animal_pos: complex
    pipes: frozendict.frozendict[complex, Pipe]

    @staticmethod
    def parse(txt: str) -> Grid:
        grid = {complex(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c != "."}
        return Grid(
            animal_pos=mi.one(p for p, c in grid.items() if c == ANIMAL),
            pipes=frozendict.frozendict((p, Pipe(c)) for p, c in grid.items() if c != ANIMAL),
        )

    def get(self, pos: complex) -> PipeGridEntry | AnimalGridEntry | None:
        if pos == self.animal_pos:
            return self.get_animal()
        pipe = self.pipes.get(pos)
        if pipe is None:
            return None
        return PipeGridEntry(pos=pos, grid=self, pipe=pipe)

    def get_animal(self) -> AnimalGridEntry:
        return AnimalGridEntry(pos=self.animal_pos, grid=self)


def part_1(txt: str) -> int:
    g = Grid.parse(txt)

    # starting from the animal, traverse along the pipe in both directions until
    # the two "pointers" meet. at that point, we've found the furthest point from
    # the start. there will always be exactly one furthest point, so we don't
    # need to worry about the pointers "crossing" without seeing one another.
    animal = g.get_animal()
    pipe_loop: set[GridEntry] = {animal}
    exploring = tuple(animal.connections())
    steps = 1
    while not mi.all_equal(exploring):
        pipe_loop.update(exploring)
        exploring = tuple(mi.one(adj for adj in entry.connections() if adj not in pipe_loop) for entry in exploring)
        steps += 1
    return steps


def part_2(txt: str) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
