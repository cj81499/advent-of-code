from typing import Callable, Generator, Iterable, List, Tuple, TypeVar

from aocd import data

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


def is_valid_parta(digits: List[int]) -> bool:
    return increasing_digits(digits) and adj_repeat(digits)


def is_valid_partb(digits: List[int]) -> bool:
    return increasing_digits(digits) and exact_adj_repeat_in_increasing(digits)


def solver(low: int, high: int, valid_func: Callable[[List[int]], bool]) -> int:
    return sum(valid_func(get_digits(n)) for n in range(low, high))


def parta(txt: str) -> int:
    low, high = (int(x) for x in txt.split("-"))
    return solver(low, high, is_valid_parta)


def partb(txt: str) -> int:
    low, high = (int(x) for x in txt.split("-"))
    return solver(low, high, is_valid_partb)


def main() -> None:
    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")


if __name__ == "__main__":
    main()
