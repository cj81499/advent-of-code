import functools
import itertools
import re

from aoc_cj import util

OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"

OPERATIONAL_PREFIX_PATTERN = re.compile(rf"^[{OPERATIONAL}]+")
DAMAGED_OR_UNKNOWN_PREFIX_PATTERN = re.compile(rf"^[{DAMAGED}{UNKNOWN}]+")


import dataclasses


@dataclasses.dataclass(frozen=True)
class Row:
    contents: str
    damaged_spring_groups: tuple[int, ...]

    @staticmethod
    def parse(s: str) -> "Row":
        contents, sep, damaged_spring_groups = s.partition(" ")
        assert sep == " "
        damaged_spring_groups = tuple(util.ints(damaged_spring_groups))
        return Row(contents, damaged_spring_groups)

    @staticmethod
    def parse2(s: str) -> "Row":
        r = Row.parse(s)
        return Row(
            UNKNOWN.join(itertools.repeat(r.contents, 5)),
            tuple(itertools.chain.from_iterable(itertools.repeat(r.damaged_spring_groups, 5))),
        )

    @functools.cache
    def count_arrangements(self) -> int:
        if len(self.contents) == 0:
            return 1 if len(self.damaged_spring_groups) == 0 else 0

        if self.contents.startswith(OPERATIONAL):
            # remove all leading operational springs
            match = OPERATIONAL_PREFIX_PATTERN.match(self.contents)
            assert match
            leading_operational_count = len(match.group(0))
            return Row(self.contents[leading_operational_count:], self.damaged_spring_groups).count_arrangements()

        if self.contents.startswith(UNKNOWN):
            return (
                Row(self.contents[1:], self.damaged_spring_groups).count_arrangements()
                + Row(DAMAGED + self.contents[1:], self.damaged_spring_groups).count_arrangements()
            )

        if self.contents.startswith(DAMAGED):
            if len(self.damaged_spring_groups) == 0:  # we weren't expecting any more damaged springs
                return 0

            match = DAMAGED_OR_UNKNOWN_PREFIX_PATTERN.match(self.contents)
            assert match
            available_damaged_spring_count = len(match.group(0))

            # the next self.damaged_spring_groups[0] springs must be damaged or unknown (assumed damaged)
            required_damaged_spring_count = self.damaged_spring_groups[0]
            if available_damaged_spring_count < required_damaged_spring_count:
                return 0

            new_contents = self.contents[required_damaged_spring_count:]
            # the first spring after the damaged spring group must be operational
            # (otherwise, it'd be part of the damaged spring group)
            if len(new_contents) > 0:
                if new_contents.startswith(DAMAGED):
                    return 0
                new_contents = new_contents[1:]

            return Row(new_contents, self.damaged_spring_groups[1:]).count_arrangements()

        assert False, "unreachable"


def part_1(txt: str) -> int:
    rows = [Row.parse(l) for l in txt.splitlines()]
    return sum(r.count_arrangements() for r in rows)


def part_2(txt: str) -> int:
    rows = [Row.parse2(l) for l in txt.splitlines()]
    return sum(r.count_arrangements() for r in rows)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
