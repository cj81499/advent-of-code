from __future__ import annotations

import re
from math import gcd, inf
from typing import List, Set, Tuple, Union

from aocd import data

# HEAVLIY inspired by:
# https://github.com/kresimir-lukin/AdventOfCode2019/blob/master/day12.py


def parta(txt: str, step_count: int = 1000) -> int:
    lines = txt.splitlines()

    positions, velocities = pos_vel(lines)
    for p, v in zip(positions, velocities):
        simulate(p, v, step_count)
    return sum(nrg(moon) for moon in zip(zip(*positions), zip(*velocities)))


def partb(txt: str) -> int:
    lines = txt.splitlines()

    positions, velocities = pos_vel(lines)
    steps_by_coord = (simulate(p, v) for p, v in zip(positions, velocities))
    return lcm(*steps_by_coord)


def pos_vel(lines: List[str]) -> Tuple[List[List[int]], List[List[int]]]:
    numbers = [(int(s) for s in re.findall(r"-?\d+", line)) for line in lines]
    positions: List[List[int]] = list(map(list, zip(*numbers)))
    velocities = [[0] * len(numbers) for _ in range(3)]  # 3 for x, y, z
    return positions, velocities


def simulate(
    positions: List[int],
    velocities: List[int],
    step_count: Union[int, float] = inf
) -> int:
    seen: Set[Tuple[int, ...]] = set()
    step = 0
    current = (*positions, *velocities)
    while (step < step_count) if step_count < inf else (current not in seen):
        seen.add(current)
        do_step(positions, velocities)
        current = (*positions, *velocities)
        step += 1
    return step


def do_step(positions: List[int], velocities: List[int]) -> None:
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


def nrg(moon: Tuple[Tuple[int, ...], ...]) -> int:
    pos, vel = moon
    p_nrg = sum(abs(n) for n in pos)
    k_nrg = sum(abs(n) for n in vel)
    return p_nrg * k_nrg


def lcm(*nums: int) -> int:
    if len(nums) == 2:
        return nums[0] * nums[1] // gcd(nums[0], nums[1])
    return lcm(nums[0], lcm(*nums[1:]))


def main() -> None:
    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")


if __name__ == "__main__":
    main()