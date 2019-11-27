from typing import Dict, List, Tuple


def distance_after_t(speed: int, flight_t: int, rest_t: int, t: int):
    return sum(speed for i in range(t) if i % (flight_t + rest_t) < flight_t)


def max_distance_after_t(reindeers: List[str], t: int = 2503):
    return max(distance_after_t(int(r[3]), int(r[6]), int(r[13]), t) for r in map(lambda r: r.split(), reindeers))


def advance_reindeers(reindeers: Dict[str, Dict[str, int]], t: int):
    for r_info in reindeers.values():
        if t % (r_info["flight_t"] + r_info["rest_t"]) < r_info["flight_t"]:
            r_info["dist"] += r_info["speed"]

    furthest_dist = max(r["dist"] for r in reindeers.values())

    for r in reindeers:
        if reindeers[r]["dist"] == furthest_dist:
            reindeers[r]["points"] += 1


def max_points_after_t(reindeers: List[str], t: int = 2503):
    reindeers = {
        r[0]: {
            "speed": int(r[3]),
            "flight_t": int(r[6]),
            "rest_t": int(r[13]),
            "dist": 0,
            "points": 0,
        }
        for r in map(lambda r: r.split(), reindeers)
    }

    for i in range(t):
        advance_reindeers(reindeers, i)

    return max(r["points"] for r in reindeers.values())


def main():
    _, input_lines = helpers.load_input(14, "Reindeer Olympics")

    print(f"part1: {max_distance_after_t(input_lines)}")
    print(f"part2: {max_points_after_t(input_lines)}")


if __name__ == "__main__":
    import helpers
    main()
