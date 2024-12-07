def part_1(txt: str) -> int:
    nums = list(map(int, txt.split(",")))
    return min(sum(abs(i - n) for n in nums) for i in range(min(nums), max(nums) + 1))


def sum_of_naturals(n: int) -> int:
    return n * (n + 1) // 2


def part_2(txt: str) -> int:
    nums = list(map(int, txt.split(",")))
    return min(sum(sum_of_naturals(abs(i - n)) for n in nums) for i in range(min(nums), max(nums) + 1))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
