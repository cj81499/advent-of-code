import functools
from collections import Counter


# This cache isn't essential, but it does speeds things up a tad bit.
@functools.cache
def advance_stone(n: int) -> tuple[int] | tuple[int, int]:
    if n == 0:
        return (1,)
    if (l := len(s := str(n))) % 2 == 0:
        return (int(s[: l // 2]), int(s[l // 2 :]))
    return (n * 2024,)


def part_1(txt: str) -> int:
    return solve(txt, blinks=25)


def part_2(txt: str) -> int:  # pragma: no cover - no test case provided
    return solve(txt, blinks=75)


def solve(txt: str, *, blinks: int) -> int:
    # for low numbers of blinks (part 1), we can simply simulate
    # for part two, the number of stones to simulate is too large.
    # observe that the order of stones does not matter
    # instead of keeping track of each stone in order, keep track of how many
    # stones we have with each number on it. that way, we can simulate all
    # stones with the same number on them at once.
    stones = Counter(map(int, txt.split()))
    for _ in range(blinks):
        new_stones = Counter[int]()
        for stone_num, count in stones.items():
            for new_stone_num in advance_stone(stone_num):
                new_stones[new_stone_num] += count
        stones = new_stones
    return stones.total()


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
