from datetime import date
from typing import Callable, Generator, Iterable, List, Tuple, TypeVar

from src.util.helpers import get_puzzle

T = TypeVar("T")


def pairwise(iterable: Iterable[T]) -> Generator[Tuple[T, T], None, None]:
    prev = None
    for current in iterable:
        if prev:
            yield (prev, current)
        prev = current


def get_digits(n: int) -> List[int]:
    return [int(i) for i in str(n)]


def adj_repeat(digits: List[int]) -> bool:
    return any(f == s for f, s in pairwise(digits))


def increasing_digits(digits: List[int]) -> bool:
    return not any(f > s for f, s in pairwise(digits))


def exact_adj_repeat_in_increasing(digits: List[int]) -> bool:
    return any(f == s and digits.count(f) == 2 for f, s in pairwise(digits))


def is_valid_part1(digits: List[int]) -> bool:
    return increasing_digits(digits) and adj_repeat(digits)


def is_valid_part2(digits: List[int]) -> bool:
    return increasing_digits(digits) and exact_adj_repeat_in_increasing(digits)


def solver(low: int, high: int, valid_func: Callable[[List[int]], bool]) -> int:
    return sum(valid_func(get_digits(n)) for n in range(low, high))


def part1(low: int, high: int) -> int:
    return solver(low, high, is_valid_part1)


def part2(low: int, high: int) -> int:
    return solver(low, high, is_valid_part2)


def main() -> None:
    txt, _ = get_puzzle(date(2019, 12, 4), "Secure Container")

    low, high = (int(x) for x in txt.split("-"))

    print(f"part1: {part1(low, high)}")
    print(f"part2: {part2(low, high)}")


if __name__ == "__main__":
    main()
