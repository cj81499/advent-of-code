import re
from collections import deque
from collections.abc import Generator, Iterable, Sequence
from dataclasses import dataclass
from functools import cached_property
from typing import ClassVar

import more_itertools as mi

from aoc_cj import util


def range_intersect(r1: range, r2: range) -> range | None:
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None


def range_difference(r1: range, r2: range) -> Generator[range, None, None]:
    if r1.start < r2.start:
        yield range(r1.start, min(r1.stop, r2.start))
    if r1.stop > r2.stop:
        yield range(max(r1.start, r2.stop), r1.stop)


@dataclass(frozen=True)
class MappingRange:
    destination_range_start: int
    source_range_start: int
    range_length: int

    @cached_property
    def source_range(self) -> range:
        return range(self.source_range_start, self.source_range_start + self.range_length)

    @staticmethod
    def parse(s: str) -> "MappingRange":
        return MappingRange(*util.ints(s))

    def contains(self, value: int) -> bool:
        return value in self.source_range

    def convert(self, value: int) -> int:
        assert self.contains(value), f"mapping range ({self}) can not map value ({value}) because it doesn't contain it"
        return self.convert_unchecked(value)

    def convert_unchecked(self, value: int) -> int:
        return value - self.source_range_start + self.destination_range_start


@dataclass(frozen=True)
class Map:
    ranges: Sequence[MappingRange]

    _HEADER_PATTERN: ClassVar = re.compile(r"(\w+)-to-(\w+) map:")

    @staticmethod
    def parse(s: str) -> "Map":
        header, *ranges = s.splitlines()
        match = Map._HEADER_PATTERN.match(header)
        assert match is not None
        ranges = [MappingRange.parse(r) for r in ranges]

        return Map(ranges)

    def convert(self, value: int) -> int:
        for mr in self.ranges:
            if mr.contains(value):
                return mr.convert(value)
        return value


def parse(txt: str) -> tuple[list[int], list[Map]]:
    seed_strs, *map_strs = txt.split("\n\n")
    seeds = list(util.ints(seed_strs))
    maps = [Map.parse(m) for m in map_strs]
    return seeds, maps


def part_1(txt: str) -> int:
    seeds, maps = parse(txt)

    values: Iterable[int] = seeds
    for m in maps:
        values = map(m.convert, values)

    return min(values)


def part_2(txt: str) -> int:
    seeds, maps = parse(txt)
    ranges = [range(start, start + length) for start, length in mi.grouper(seeds, 2, incomplete="strict")]

    for map in maps:
        new_ranges: list[range] = []
        for full_r in ranges:
            to_map = deque((full_r,))
            while to_map:
                r = to_map.popleft()

                mr_intersection = mi.first(
                    ((mr, isect) for mr in map.ranges if (isect := range_intersect(r, mr.source_range)) is not None),
                    None,
                )

                if mr_intersection is None:
                    # no mr overlaps w/ r, map it thru as-is
                    new_ranges.append(r)
                else:
                    # at least one mr overlaps w/ r. map the overlapping part and handle the non-overlapping parts later
                    mr, intersection = mr_intersection
                    new_ranges.append(range(mr.convert(intersection.start), mr.convert_unchecked(intersection.stop)))
                    to_map.extend(range_difference(r, mr.source_range))
        ranges = new_ranges

    return min(r.start for r in ranges)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
