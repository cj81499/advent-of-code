from dataclasses import dataclass
from typing import Union

import more_itertools as mi


@dataclass
class SectionAssignment:
    start: int
    end: int

    @staticmethod
    def parse(s: str) -> "SectionAssignment":
        return SectionAssignment(*map(int, s.split("-")))

    def __contains__(self, item: Union[int, "SectionAssignment"]) -> bool:
        if isinstance(item, int):
            return self.start <= item <= self.end
        return item.start in self and item.end in self


@dataclass
class SectionAssignmentPair:
    left: SectionAssignment
    right: SectionAssignment

    @staticmethod
    def parse(s: str) -> "SectionAssignmentPair":
        return SectionAssignmentPair(*map(SectionAssignment.parse, s.split(",")))

    def full_overlap(self) -> bool:
        return self.left in self.right or self.right in self.left

    def partial_overlap(self) -> bool:
        return (
            self.left.start in self.right
            or self.left.end in self.right
            or self.right.start in self.left
            or self.right.end in self.left
        )


def part_1(txt: str) -> int:
    return mi.ilen(1 for line in txt.splitlines() if SectionAssignmentPair.parse(line).full_overlap())


def part_2(txt: str) -> int:
    return mi.ilen(1 for line in txt.splitlines() if SectionAssignmentPair.parse(line).partial_overlap())


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
