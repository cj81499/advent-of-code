import math


def parta(txt):
    arrival_time, bus_ids = txt.splitlines()
    arrival_time = int(arrival_time)
    bus_ids = bus_ids.split(",")
    bus_ids = [int(x) for x in bus_ids if x != "x"]
    earliest = (float("inf"), None)
    for bus_id in bus_ids:
        bus_departure_time = arrival_time - (arrival_time % bus_id) + bus_id
        if bus_departure_time < earliest[0]:
            earliest = (bus_departure_time, bus_id)
    earliest_bus = earliest[1]
    wait_time = earliest[0] - arrival_time
    return earliest_bus * wait_time


def bus_leaves_at(bus_id, t):
    if t == 0:
        return True
    return t % bus_id == 0


def lcm(nums):
    first, *rest = nums
    if len(rest) == 0:
        return first
    lcm_rest = lcm(rest)
    return (first * lcm_rest) // math.gcd(first, lcm_rest)


def partb(txt):
    _, bus_ids = txt.splitlines()
    bus_ids = bus_ids.split(",")

    t = 0
    for i, bus_id in enumerate(bus_ids):
        if i == 0 or bus_id == "x":
            continue
        step_size = lcm(int(id) for id in bus_ids[:i] if id != "x")
        while not bus_leaves_at(int(bus_id), t + i):
            t += step_size
    return t


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
