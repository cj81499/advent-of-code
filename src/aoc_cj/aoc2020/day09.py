from collections import deque
from itertools import combinations


def parse_nums(txt):
    return [int(line) for line in txt.splitlines()]


def parta(txt, preamble_size=25):
    nums = parse_nums(txt)
    d = deque()
    for num in nums:
        if len(d) > preamble_size:
            if not any(x + y == num for x, y in combinations(d, 2)):
                return num
            d.popleft()
        d.append(num)
    return -1


def partb(txt, preamble_size=25):
    parta_ans = parta(txt, preamble_size=preamble_size)
    nums = parse_nums(txt)
    for start in range(len(nums)):
        size = 2
        while (s := sum(nums[start : start + size])) < parta_ans:
            size += 1
        if s == parta_ans:
            return min(nums[start : start + size]) + max(nums[start : start + size])
    return -1


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
