import dataclasses
import itertools
from collections.abc import Collection, Generator, Iterable
from typing import Self

import more_itertools as mi
from more_itertools import ilen


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Database:
    fresh_ranges: frozenset[range]
    available_ids: frozenset[int]

    @classmethod
    def parse(cls, txt: str) -> Self:
        fresh_ranges, available_ids = txt.split("\n\n")
        return cls(
            fresh_ranges=frozenset(cls._parse_ranges(fresh_ranges.splitlines())),
            available_ids=frozenset(int(l) for l in available_ids.splitlines()),
        )

    @staticmethod
    def _parse_ranges(fresh_ranges: list[str]) -> Generator[range]:
        for r in fresh_ranges:
            l, sep, r = r.partition("-")
            assert sep == "-", f"{sep=} {r=}"
            yield range(int(l), int(r) + 1)

    def fresh_available_ids(self) -> Generator[int]:
        for id in self.available_ids:
            if any(id in r for r in self.fresh_ranges):
                yield id

    def all_fresh_ids(self) -> Generator[int]:
        # trival, technically correct, but _far_ too slow for real input
        yield from mi.unique_everseen(itertools.chain.from_iterable(self.fresh_ranges))


def part_1(txt: str) -> int:
    d = Database.parse(txt)
    return ilen(d.fresh_available_ids())


def part_2(txt: str) -> int:
    d = Database.parse(txt)
    merged = merge_ranges(d.fresh_ranges)
    return sum(len(r) for r in merged)
    return ilen(d.all_fresh_ids())


def merge_ranges(ranges: Iterable[range]) -> Collection[range]:
    sorted_ranges = sorted(ranges, key=lambda r: (r.start, r.stop, r.step))
    current = range(0, 0)  # empty range
    merged = set[range]()
    for r in sorted_ranges:
        if r.start in current:
            current = range(current.start, max(current.stop, r.stop))
        else:
            merged.add(current)
            current = r
    merged.add(current)
    return merged


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
