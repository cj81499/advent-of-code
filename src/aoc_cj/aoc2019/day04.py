import itertools


def get_digits(n: int) -> list[int]:
    return [int(i) for i in str(n)]


def adj_repeat(digits: list[int]) -> bool:
    return any(f == s for f, s in itertools.pairwise(digits))


def increasing_digits(digits: list[int]) -> bool:
    return not any(f > s for f, s in itertools.pairwise(digits))


def exact_adj_repeat_in_increasing(digits: list[int]) -> bool:
    return any(f == s and digits.count(f) == 2 for f, s in itertools.pairwise(digits))


def is_valid_part_1(digits: list[int]) -> bool:
    return increasing_digits(digits) and adj_repeat(digits)


def is_valid_part_2(digits: list[int]) -> bool:
    return increasing_digits(digits) and exact_adj_repeat_in_increasing(digits)


def solver(low: int, high: int, is_valid) -> int:
    return sum(is_valid(get_digits(n)) for n in range(low, high))


def part_1(txt: str) -> int:
    low, high = (int(x) for x in txt.split("-"))
    return solver(low, high, is_valid_part_1)


def part_2(txt: str) -> int:
    low, high = (int(x) for x in txt.split("-"))
    return solver(low, high, is_valid_part_2)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
