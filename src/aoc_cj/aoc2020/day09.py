from collections import deque
from itertools import combinations


def parse_nums(txt):
    return [int(line) for line in txt.splitlines()]


def part_1(txt, preamble_size=25):
    nums = parse_nums(txt)
    d = deque()
    for num in nums:
        if len(d) > preamble_size:
            if not any(x + y == num for x, y in combinations(d, 2)):
                return num
            d.popleft()
        d.append(num)
    return -1


def part_2(txt, preamble_size=25):
    part_1_ans = part_1(txt, preamble_size=preamble_size)
    nums = parse_nums(txt)
    for start in range(len(nums)):
        size = 2
        while (s := sum(nums[start : start + size])) < part_1_ans:
            size += 1
        if s == part_1_ans:
            return min(nums[start : start + size]) + max(nums[start : start + size])
    return -1


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
