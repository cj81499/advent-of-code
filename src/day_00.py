from datetime import date
from typing import List

from src.util.helpers import get_puzzle


def part1(txt: str, lines: List[str]) -> int:
    return 0


def part2(txt: str, lines: List[str]) -> int:
    return 0


def main() -> None:
    txt, lines = get_puzzle(date(2019, 12, 0), "")  # noqa

    print(f"part1: {part1(txt, lines)}")
    print(f"part2: {part2(txt, lines)}")


if __name__ == "__main__":
    main()
