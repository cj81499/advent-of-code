import dataclasses
from collections.abc import Generator, Iterable
from typing import Self

from aoc_cj import util


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Database:
    fresh_ranges: frozenset[range]
    available_ids: frozenset[int]

    @classmethod
    def parse(cls, txt: str) -> Self:
        fresh_ranges, available_ids = txt.split("\n\n")
        return cls(
            fresh_ranges=frozenset(map(util.parse_range, fresh_ranges.splitlines())),
            available_ids=frozenset(map(int, available_ids.splitlines())),
        )


def part_1(txt: str) -> int:
    d = Database.parse(txt)
    return sum(1 for id_ in d.available_ids if any(id_ in r for r in d.fresh_ranges))


def part_2(txt: str) -> int:
    d = Database.parse(txt)
    return sum(map(len, merge_ranges(d.fresh_ranges)))


def merge_ranges(ranges: Iterable[range]) -> Generator[range]:
    sorted_ranges = sorted(ranges, key=lambda r: (r.start, r.stop, r.step))
    if len(sorted_ranges) <= 0:
        return
    current = range(0)  # empty range
    for r in sorted_ranges:
        if r.start in current:
            current = range(current.start, max(current.stop, r.stop))
        else:
            yield current
            current = r
    yield current


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
