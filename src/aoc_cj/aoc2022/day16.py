import dataclasses
import re
from collections import deque

Valves = dict[str, tuple[int, set[str]]]

MAX_TIME = 30

indent = 0


@dataclasses.dataclass(frozen=True)
class Valve:
    name: str
    flow_rate: int
    tunnels_to: frozenset[str]

    PARSE_REGEX = re.compile(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)")

    @staticmethod
    def parse(valve: str) -> "Valve":
        m = Valve.PARSE_REGEX.match(valve)
        assert m is not None
        name, flow_rate, tunnels_to = m.groups()
        return Valve(name, int(flow_rate), frozenset(tunnels_to.split(", ")))


def parta(txt: str) -> int:
    valves = {(valve := Valve.parse(l)).name: valve for l in txt.splitlines()}

    # observation: many valves have flow rate 0.
    # idea: skip simulating valves that we'll never open
    valve_graph_steps_between: dict[str, dict[str, int]] = {}
    for valve in valves.values():
        if valve.name == "AA" or valve.flow_rate != 0:
            # find # of steps to all other valves
            initial = (0, valve.name)
            q = deque([initial])
            steps_to: dict[str, int] = valve_graph_steps_between.setdefault(valve.name, {})
            while q:
                step_count, name = q.popleft()

                if name not in steps_to:
                    steps_to[name] = step_count
                steps_to[name] = min(step_count, steps_to[name])

                for adj_valve in valves[name].tunnels_to:
                    if adj_valve not in steps_to:
                        q.append((step_count + 1, adj_valve))

            # never try to go from a location to that same location
            del steps_to[valve.name]
            # never try to go to a location where there is not a valve w/ flow rate
            to_remove = {name for name in steps_to if valves[name].flow_rate == 0}
            for name in to_remove:
                del steps_to[name]

    def explore(
        pos: str = "AA",
        remaining_time: int = MAX_TIME,
        closed_valves: frozenset[str] = frozenset(valve_graph_steps_between).difference(("AA",)),
    ) -> int:
        if remaining_time <= 0:
            return 0

        if pos in closed_valves:
            return (
                explore(pos, remaining_time - 1, closed_valves.difference((pos,)))
                + (remaining_time - 1) * valves[pos].flow_rate
            )

        results = (explore(v, remaining_time - valve_graph_steps_between[pos][v], closed_valves) for v in closed_valves)
        return max(results, default=0)

    return explore()


def partb(txt: str) -> None:
    return None


EXAMPLE_INPUT = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
""".strip()

if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
