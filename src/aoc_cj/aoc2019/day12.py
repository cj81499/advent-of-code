import re
from math import gcd, inf

# HEAVLIY inspired by:
# https://github.com/kresimir-lukin/AdventOfCode2019/blob/master/day12.py


def part_1(txt: str, step_count: int = 1000) -> int:
    lines = txt.splitlines()

    positions, velocities = pos_vel(lines)
    for p, v in zip(positions, velocities):
        simulate(p, v, step_count)
    return sum(nrg(moon) for moon in zip(zip(*positions), zip(*velocities)))


def part_2(txt: str) -> int:
    lines = txt.splitlines()

    positions, velocities = pos_vel(lines)
    steps_by_coord = (simulate(p, v) for p, v in zip(positions, velocities))
    return lcm(*steps_by_coord)


def pos_vel(lines: list[str]) -> tuple[list[list[int]], list[list[int]]]:
    numbers = [(int(s) for s in re.findall(r"-?\d+", line)) for line in lines]
    positions: list[list[int]] = list(map(list, zip(*numbers)))
    velocities = [[0] * len(numbers) for _ in range(3)]  # 3 for x, y, z
    return positions, velocities


def simulate(positions: list[int], velocities: list[int], step_count=inf) -> int:
    seen: set[tuple[int, ...]] = set()
    step = 0
    current = (*positions, *velocities)
    while (step < step_count) if step_count < inf else (current not in seen):
        seen.add(current)
        do_step(positions, velocities)
        current = (*positions, *velocities)
        step += 1
    return step


def do_step(positions: list[int], velocities: list[int]) -> None:
    for i, pos in enumerate(positions):
        velocities[i] += sum(compare(pos, other) for other in positions)
    for i, vel in enumerate(velocities):
        positions[i] += vel


def compare(a: int, b: int) -> int:
    if a < b:
        return 1
    if a > b:
        return -1
    return 0


def nrg(moon: tuple[tuple[int, ...], ...]) -> int:
    pos, vel = moon
    p_nrg = sum(abs(n) for n in pos)
    k_nrg = sum(abs(n) for n in vel)
    return p_nrg * k_nrg


def lcm(*nums: int) -> int:
    if len(nums) == 2:
        return nums[0] * nums[1] // gcd(nums[0], nums[1])
    return lcm(nums[0], lcm(*nums[1:]))


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
