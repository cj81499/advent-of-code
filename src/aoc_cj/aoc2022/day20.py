from collections import deque

from aoc_cj import util


def part_1(txt: str, *, decryption_key: int = 1, rounds: int = 1) -> int:
    d = deque((n * decryption_key, i) for i, n in enumerate(util.ints(txt)))

    for _ in range(rounds):
        for i in range(len(d)):
            while d[0][1] != i:
                d.rotate(-1)
            n, j = d.popleft()
            assert i == j
            d.rotate(-n)
            d.appendleft((n, i))
            d.rotate(n)

    nums = [n for n, _i in d]
    zero_idx = nums.index(0)

    return sum(nums[(zero_idx + i * 1000) % len(nums)] for i in range(1, 4))


def part_2(txt: str) -> int:
    return part_1(txt, decryption_key=811589153, rounds=10)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
