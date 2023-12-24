import dataclasses
import itertools
import re
from typing import ClassVar

from aoc_cj import util


@dataclasses.dataclass(frozen=True)
class Card:
    winning_nums: frozenset[int]
    nums_you_have: frozenset[int]

    _PATTERN: ClassVar = re.compile(r"Card +\d+: ([\d ]+) \| ([\d ]+)")

    @staticmethod
    def parse(s: str) -> "Card":
        match = Card._PATTERN.match(s)
        assert match, f"Failed to parse Card ({s})"
        winning_nums = frozenset(util.ints(match.group(1)))
        nums_you_have = frozenset(util.ints(match.group(2)))
        return Card(winning_nums, nums_you_have)

    def points(self) -> int:
        match_count = self.match_count()
        if match_count == 0:
            return 0
        res = 2 ** (match_count - 1)
        # matching_nums_count is known to be a positive integer,
        # so matching_nums_count - 1 is a non-negative integer,
        # so 2 ** (matching_nums_count - 1) must be an integer.
        assert isinstance(res, int)
        return res

    def match_count(self) -> int:
        return len(self.winning_nums.intersection(self.nums_you_have))


def part_1(txt: str) -> int:
    cards = (Card.parse(l) for l in txt.splitlines())
    return sum(c.points() for c in cards)


@dataclasses.dataclass
class CardCount:
    card: Card
    copy_count: int = 1  # at the start, we have 1 copy of each card


def part_2(txt: str) -> int:
    cards = [CardCount(Card.parse(l)) for l in txt.splitlines()]

    for i, current in enumerate(cards):
        # let N be the number of copies of the current card
        # let M be the number of matching numbers on the current card
        # win N copies of the next M cards
        for next_card in itertools.islice(cards, i + 1, i + 1 + current.card.match_count()):
            next_card.copy_count += current.copy_count

    total_card_count = sum(cc.copy_count for cc in cards)
    return total_card_count


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
