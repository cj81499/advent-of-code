import dataclasses
import heapq
import itertools
import re


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


def parse(txt: str) -> tuple[dict[str, Valve], dict[tuple[str, str], int]]:
    valves = {(valve := Valve.parse(l)).name: valve for l in txt.splitlines()}

    steps_between: dict[tuple[str, str], int] = {}
    for v in valves.values():
        h = [(0, v.name)]
        while h:
            step_count, name = heapq.heappop(h)
            if (t := (v.name, name)) not in steps_between or step_count < steps_between[t]:
                steps_between[t] = step_count

                for adj_valve in valves[name].tunnels_to:
                    heapq.heappush(h, (step_count + 1, adj_valve))

    # many valves have flow rate 0.
    # skip simulating valves that we'll never open
    valves_with_nonzero_flow = {name for name, valve in valves.items() if valve.flow_rate != 0}
    steps_between = {
        (a, b): v
        for (a, b), v in steps_between.items()
        if a != b and (a == "AA" or (a in valves_with_nonzero_flow and b in valves_with_nonzero_flow))
    }

    return valves, steps_between


def parta(txt: str) -> int:
    valves, steps_between = parse(txt)

    def explore(destination: str, t_to_destination: int, remaining_time: int, closed_valves: frozenset[str]) -> int:
        if remaining_time <= 0:
            return 0

        if t_to_destination == 0:
            if destination in closed_valves:
                result = explore(destination, 0, remaining_time - 1, closed_valves.difference((destination,)))
                return result + (remaining_time - 1) * valves[destination].flow_rate

            results = (
                explore(v, steps_between[destination, v] - 1, remaining_time - 1, closed_valves) for v in closed_valves
            )
            return max(results, default=0)

        return explore(destination, t_to_destination - 1, remaining_time - 1, closed_valves)

    return explore("AA", 0, 30, frozenset(name for name, v in valves.items() if v.flow_rate != 0))


def partb(txt: str) -> int:
    # raise NotImplementedError()
    valves, steps_between = parse(txt)
    initial_closed_valves = frozenset(name for name, v in valves.items() if v.flow_rate != 0)

    def explore(
        my_destination: str,
        t_to_my_destination: int,
        ele_destination: str,
        t_to_ele_destination: int,
        remaining_time: int,
        closed_valves: frozenset[str],
    ) -> int:
        if remaining_time <= 0:
            return 0

        # only time that ele and i should be at same location is at start of simulation
        assert my_destination != ele_destination or (
            my_destination == "AA" and ele_destination == "AA"
        ), f"{my_destination}, {ele_destination}"

        at_my_destination = t_to_my_destination == 0
        at_ele_destination = t_to_ele_destination == 0

        my_valve_is_closed = my_destination in closed_valves
        ele_valve_is_closed = ele_destination in closed_valves

        if at_my_destination and at_ele_destination:
            if my_valve_is_closed and ele_valve_is_closed:
                # both need to open valves
                return explore(
                    my_destination,
                    0,
                    ele_destination,
                    0,
                    remaining_time - 1,
                    closed_valves.difference((my_destination, ele_destination)),
                ) + (remaining_time - 1) * (valves[my_destination].flow_rate + valves[ele_destination].flow_rate)

            if my_valve_is_closed:
                # i open valve, ele needs new destination
                results = (
                    explore(
                        my_destination,
                        0,
                        v,
                        steps_between[ele_destination, v] - 1,
                        remaining_time - 1,
                        closed_valves.difference((my_destination,)),
                    )
                    for v in closed_valves.difference((my_destination, ele_destination))
                )
                return max(results, default=0) + (remaining_time - 1) * valves[my_destination].flow_rate

            if ele_valve_is_closed:
                # i need new destination, ele opens valve
                results = (
                    explore(
                        v,
                        steps_between[my_destination, v] - 1,
                        ele_destination,
                        0,
                        remaining_time - 1,
                        closed_valves.difference((ele_destination,)),
                    )
                    for v in closed_valves.difference((my_destination, ele_destination)).difference(
                        (my_destination, ele_destination)
                    )
                )
                return max(results, default=0) + (remaining_time - 1) * valves[ele_destination].flow_rate
            # neither valve is closed
            # both need new destinations
            best_result = 0
            for v1, v2 in itertools.permutations(closed_valves, 2):
                best_result = max(
                    best_result,
                    explore(
                        v1,
                        steps_between[my_destination, v1] - 1,
                        v2,
                        steps_between[my_destination, v2] - 1,
                        remaining_time - 1,
                        closed_valves,
                    ),
                )
            return best_result
            # raise NotImplementedError()

        if at_my_destination:
            if my_valve_is_closed:
                result = explore(
                    my_destination,
                    0,
                    ele_destination,
                    t_to_ele_destination - 1,
                    remaining_time - 1,
                    closed_valves.difference((my_destination,)),
                )
                return result + (remaining_time - 1) * valves[my_destination].flow_rate

            results = (
                explore(
                    v,
                    steps_between[my_destination, v] - 1,
                    ele_destination,
                    t_to_ele_destination - 1,
                    remaining_time - 1,
                    closed_valves,
                )
                for v in closed_valves.difference((my_destination, ele_destination))
            )
            return max(results, default=0)

        if at_ele_destination:
            if ele_valve_is_closed:
                result = explore(
                    my_destination,
                    t_to_my_destination - 1,
                    ele_destination,
                    0,
                    remaining_time - 1,
                    closed_valves.difference((ele_destination,)),
                )
                return result + (remaining_time - 1) * valves[ele_destination].flow_rate

            results = (
                explore(
                    my_destination,
                    t_to_my_destination - 1,
                    v,
                    steps_between[ele_destination, v] - 1,
                    remaining_time - 1,
                    closed_valves,
                )
                for v in closed_valves.difference((my_destination, ele_destination))
            )
            return max(results, default=0)

        m = min(t_to_my_destination, t_to_ele_destination)
        return explore(
            my_destination,
            t_to_my_destination - m,
            ele_destination,
            t_to_ele_destination - m,
            remaining_time - m,
            closed_valves,
        )

    return explore("AA", 0, "AA", 0, 26, initial_closed_valves)


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

    # data = EXAMPLE_INPUT

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
