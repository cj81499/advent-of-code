import itertools
from collections.abc import Sequence
from dataclasses import dataclass

from aoc_cj import util


@dataclass
class History:
    nums: Sequence[int]

    def next_value(self) -> int:
        if all(n == 0 for n in self.nums):
            return 0
        return self.nums[-1] + History(self._differences()).next_value()

    def prev_value(self) -> int:
        if all(n == 0 for n in self.nums):
            return 0
        return self.nums[0] - History(self._differences()).prev_value()

    def _differences(self) -> Sequence[int]:
        return [b - a for a, b in itertools.pairwise(self.nums)]


def part_1(txt: str) -> int:
    histories = (History(tuple(util.ints(l))) for l in txt.splitlines())
    return sum(h.next_value() for h in histories)


def part_2(txt: str) -> int:
    histories = (History(tuple(util.ints(l))) for l in txt.splitlines())
    return sum(h.prev_value() for h in histories)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
