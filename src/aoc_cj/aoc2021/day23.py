import dataclasses
import itertools
from typing import Iterable, Optional

from aoc_cj.util.heap import Heap

COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}

Spot = Optional[str]


@dataclasses.dataclass(frozen=True)
class Room:
    top: Spot
    bottom: Spot

    @property
    def EMPTY_ROOM():
        return Room(None, None)


@dataclasses.dataclass(frozen=True)
class State:
    rooms: tuple[Room, Room, Room, Room]
    hallway: tuple[Spot, Spot, Spot, Spot, Spot, Spot, Spot, Spot, Spot, Spot, Spot]

    def next_states(self) -> Iterable[tuple[int, "State"]]:
        # for each Amphipod
        #   for each move that Amphipod can make
        #       yield the energy cost of the move and the State representing the move

        # 1. Amphipods will never stop on the space immediately outside any room.

        # therefore, never return a state w/ an Amphipod in hallway[2], hallway[4], hallway[6], or hallway[8]

        # 2. Amphipods will never move from the hallway into a room unless that room is
        # their destination room and that room contains no amphipods which do not also
        # have that room as their own destination

        # 3. Once an amphipod stops moving in the hallway, it will stay in that spot
        # until it can move into a room.

        yield from ()

    @classmethod
    def parse(cls, txt: str):
        columns = zip(*txt.splitlines())
        room_contents = (col[2:4] for col in itertools.islice(columns, 3, 10, 2))
        rooms = tuple(Room(t, b) for t, b in room_contents)
        return cls(rooms, tuple([None] * 11))


GOAL = State(
    (Room("A", "A"), Room("B", "B"), Room("C", "C"), Room("D", "D")),
    tuple([None] * 11),
)


def parta(txt: str) -> None:
    print(txt)
    h = Heap([(0, State.parse(txt))])
    while h:
        energy, s = h.pop()
        if s == GOAL:
            return energy
        print(s)
        for cost, next_s in s.next_states():
            h.push((energy + cost, next_s))
    assert False, "did not reach goal"


def partb(txt: str) -> None:
    return None


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
