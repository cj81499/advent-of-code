def distance_after_t(speed: int, flight_t: int, rest_t: int, t: int):
    return sum(speed for i in range(t) if i % (flight_t + rest_t) < flight_t)


def max_distance_after_t(reindeers: list[str], t: int):
    return max(distance_after_t(int(r[3]), int(r[6]), int(r[13]), t) for r in map(lambda r: r.split(), reindeers))


def advance_reindeers(reindeers: dict[str, dict[str, int]], t: int):
    for r_info in reindeers.values():
        if t % (r_info["flight_t"] + r_info["rest_t"]) < r_info["flight_t"]:
            r_info["dist"] += r_info["speed"]

    furthest_dist = max(r["dist"] for r in reindeers.values())

    for r in reindeers:
        if reindeers[r]["dist"] == furthest_dist:
            reindeers[r]["points"] += 1


def max_points_after_t(reindeers: list[str], t: int):
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


def parta(txt, t: int = 2503):
    return max_distance_after_t(txt.splitlines(), t)


def partb(txt, t: int = 2503):
    return max_points_after_t(txt.splitlines(), t)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
