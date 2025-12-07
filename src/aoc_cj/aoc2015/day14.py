import dataclasses
from collections.abc import Generator, Mapping
from typing import Self

import more_itertools as mi


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Reindeer:
    name: str
    fly_speed: int  # in km/s
    fly_duration: int
    rest_duration: int

    @classmethod
    def parse(cls, s: str) -> Self:
        split = s.split()
        return cls(
            name=split[0],
            fly_speed=int(split[3]),
            fly_duration=int(split[6]),
            rest_duration=int(split[13]),
        )


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class ReindeerState:
    is_flying: bool
    remaining_duration: int
    distance_traveled: int = 0


def race_reindeers(reindeers: set[Reindeer]) -> Generator[Mapping[Reindeer, ReindeerState]]:
    state = {r: ReindeerState(is_flying=False, remaining_duration=0) for r in reindeers}
    while True:
        new_state = {}
        for r, s in state.items():
            remaining_duration = s.remaining_duration - 1
            is_flying = s.is_flying
            distance_traveled = s.distance_traveled

            if remaining_duration <= 0:
                remaining_duration = r.rest_duration if s.is_flying else r.fly_duration
                is_flying = not is_flying

            if is_flying:
                distance_traveled += r.fly_speed

            new_state[r] = ReindeerState(
                is_flying=is_flying,
                remaining_duration=remaining_duration,
                distance_traveled=distance_traveled,
            )
        state = new_state
        yield state


def part_1(txt: str, *, duration: int = 2503) -> int:
    reindeers = set(map(Reindeer.parse, txt.splitlines()))
    race_simulation = race_reindeers(reindeers)
    final_state = mi.nth(race_simulation, duration)  # get simulation state after duration seconds
    assert final_state is not None, "simulation could go on forever"
    return max(rs.distance_traveled for rs in final_state.values())


def part_2(txt: str, *, duration: int = 2503) -> int:
    reindeers = set(map(Reindeer.parse, txt.splitlines()))
    race_simulation = race_reindeers(reindeers)
    points = {r.name: 0 for r in reindeers}
    for _ in range(duration + 1):
        state = next(race_simulation)
        max_distance_traveled = max(s.distance_traveled for s in state.values())
        leading_reindeers = {r for r, s in state.items() if s.distance_traveled == max_distance_traveled}
        for r in leading_reindeers:
            points[r.name] += 1
    return max(points.values())


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
