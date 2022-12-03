from more_itertools import pairwise


def get_digits(n: int) -> list[int]:
    return [int(i) for i in str(n)]


def adj_repeat(digits: list[int]) -> bool:
    return any(f == s for f, s in pairwise(digits))


def increasing_digits(digits: list[int]) -> bool:
    return not any(f > s for f, s in pairwise(digits))


def exact_adj_repeat_in_increasing(digits: list[int]) -> bool:
    return any(f == s and digits.count(f) == 2 for f, s in pairwise(digits))


def is_valid_parta(digits: list[int]) -> bool:
    return increasing_digits(digits) and adj_repeat(digits)


def is_valid_partb(digits: list[int]) -> bool:
    return increasing_digits(digits) and exact_adj_repeat_in_increasing(digits)


def solver(low: int, high: int, is_valid) -> int:
    return sum(is_valid(get_digits(n)) for n in range(low, high))


def parta(txt: str) -> int:
    low, high = (int(x) for x in txt.split("-"))
    return solver(low, high, is_valid_parta)


def partb(txt: str) -> int:
    low, high = (int(x) for x in txt.split("-"))
    return solver(low, high, is_valid_partb)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
