import functools
import itertools
from collections import Counter


@functools.cache
def advance_stone(n: int) -> tuple[int] | tuple[int, int]:
    if n == 0:
        return (1,)
    if (l := len(s := str(n))) % 2 == 0:
        return (int(s[: l // 2]), int(s[l // 2 :]))
    return (n * 2024,)


def part_1(txt: str) -> int:
    # original solution
    nums = tuple(map(int, txt.split()))
    for _ in range(25):
        nums = tuple(itertools.chain.from_iterable(map(advance_stone, nums)))
    return len(nums)


def part_2(txt: str) -> int:
    return solve(txt, blinks=75)


def solve(txt: str, *, blinks: int) -> int:
    stones = Counter(map(int, txt.split()))
    for _ in range(blinks):
        new_stones = Counter[int]()
        for s, count in stones.items():
            for new_stone in advance_stone(s):
                new_stones[new_stone] += count
        stones = new_stones
    return stones.total()


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
