from datetime import date
from typing import List

from src.util.helpers import get_puzzle


def fuel_req(mass: int) -> int:
    return mass // 3 - 2


def fuel_req_rec(mass: int) -> int:
    r = fuel_req(mass)
    return 0 if 0 >= r else r + fuel_req_rec(r)


def part1(nums: List[int]) -> int:
    return sum(fuel_req(x) for x in nums)


def part2(nums: List[int]) -> int:
    return sum(fuel_req_rec(x) for x in nums)


def main() -> None:
    _, lines = get_puzzle(date(2019, 12, 1), "The Tyranny of the Rocket Equation")  # noqa
    nums = [int(x) for x in lines]

    print(f"part1: {part1(nums)}")
    print(f"part2: {part2(nums)}")


if __name__ == "__main__":
    main()
