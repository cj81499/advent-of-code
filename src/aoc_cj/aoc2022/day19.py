import dataclasses
import enum
import itertools
import re
from collections import Counter
from collections.abc import Generator, Iterable

import more_itertools as mi

from aoc_cj import util


class Resource(enum.Enum):
    ORE = enum.auto()
    CLAY = enum.auto()
    OBSIDIAN = enum.auto()
    GEODE = enum.auto()


@dataclasses.dataclass(frozen=True)
class Blueprint:
    blueprint_n: int

    robot_costs: dict[Resource, Counter[Resource]]

    _PARSE_PATTERN = re.compile(
        r"Each (?P<robot_type>\w+) robot costs (?P<mat1_cost>\d+) (?P<mat1_type>\w+)(\.| and (?P<mat2_cost>\d+) (?P<mat2_type>\w+)\.)"
    )

    @staticmethod
    def parse(blueprint: str) -> "Blueprint":

        blueprint_n = mi.first(util.ints(blueprint))

        robot_costs: dict[Resource, Counter[Resource]] = {}

        for m in Blueprint._PARSE_PATTERN.finditer(blueprint):
            robot_cost = Counter({Resource[m.group("mat1_type").upper()]: int(m.group("mat1_cost"))})
            if (mat2_cost := m.group("mat2_cost")) is not None:
                assert (mat2_type := m.group("mat2_type")) is not None
                robot_cost[Resource[mat2_type.upper()]] = int(mat2_cost)

            robot_costs[Resource[m.group("robot_type").upper()]] = robot_cost

        return Blueprint(blueprint_n, robot_costs)

    def simulate(self, *, duration: int = 24) -> int:
        start = SimulationState(Counter([Resource.ORE]), Counter(), Counter())

        states: Iterable[SimulationState] = [start]
        for i in range(duration):
            print(
                i,
                len(states),
                max(s.resources[Resource.OBSIDIAN] for s in states),
                max(s.resources[Resource.GEODE] for s in states),
            )
            states = [*itertools.chain.from_iterable(s.next_states(self) for s in states)]

        # print(mi.ilen(states))

        return max(s.resources[Resource.GEODE] for s in states)

        # next_states = [*itertools.chain.from_iterable(s.next_states(self) for s in states)]
        # print(1)
        # pp(next_states)
        # print()

        # next_states = [*itertools.chain.from_iterable(s.next_states(self) for s in next_states)]
        # print(2)
        # pp(next_states)
        # print()

        # next_states = [*itertools.chain.from_iterable(s.next_states(self) for s in next_states)]
        # print(3)
        # pp(next_states)
        # print()

        # next_states = [*itertools.chain.from_iterable(s.next_states(self) for s in next_states)]
        # print(4)
        # pp(next_states)
        # print()

        # next_states = [*itertools.chain.from_iterable(s.next_states(self) for s in next_states)]
        # print(5)
        # pp(next_states)
        # print()

        # print(self.robot_costs)


@dataclasses.dataclass(frozen=True)
class SimulationState:
    robots: Counter[Resource]
    resources: Counter[Resource]
    building: Counter[Resource]

    def next_states(self, blueprint: Blueprint) -> Generator["SimulationState", None, None]:
        # simulate where we've built each robot type we could afford
        for robot_type, robot_cost in blueprint.robot_costs.items():
            can_afford = all(self.resources[mat] >= mat_cost for mat, mat_cost in robot_cost.items())
            if can_afford:
                if robot_type == Resource.GEODE:
                    print(f"  {self} -> {'can' if can_afford else 'can not'} afford {robot_type}")
                yield from SimulationState(
                    self.robots,
                    self.resources - robot_cost,
                    self.building + Counter([robot_type]),
                ).next_states(blueprint)

        # simulate building nothing
        yield SimulationState(
            self.robots + self.building,
            self.resources + self.robots,
            Counter(),
        )


def parta(txt: str) -> int:
    blueprints = [Blueprint.parse(l) for l in txt.splitlines()]

    return sum(b.blueprint_n * b.simulate() for b in blueprints)


def partb(txt: str) -> None:
    return None


EXAMPLE_INPUT = (
    """
Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.
""".strip()
    .replace("\n  ", " ")
    .replace("\n\n", "\n")
)

if __name__ == "__main__":
    from aocd import data

    data = EXAMPLE_INPUT

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
