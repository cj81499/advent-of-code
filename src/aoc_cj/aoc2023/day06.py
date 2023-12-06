import dataclasses
import math

import more_itertools as mi

from aoc_cj import util


@dataclasses.dataclass(frozen=True)
class Race:
    time: int
    distance: int

    def ways_to_win(self) -> int:
        wins = 0
        for move_speed in range(self.time):
            move_duration = self.time - move_speed
            total_distance = move_speed * move_duration
            if total_distance > self.distance:
                wins += 1
        return wins


def parta(txt: str) -> int:
    times, distances = (tuple(util.ints(l)) for l in txt.splitlines())
    races = [Race(t, d) for t, d in mi.zip_equal(times, distances)]
    return math.prod(r.ways_to_win() for r in races)


def partb(txt: str) -> int:
    time, distance = (mi.one(util.ints(l.split(":")[1])) for l in txt.replace(" ", "").splitlines())
    r = Race(time, distance)
    return r.ways_to_win()


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
