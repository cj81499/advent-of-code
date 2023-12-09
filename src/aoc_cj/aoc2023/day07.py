import enum
import functools
from collections import Counter
from dataclasses import dataclass
from functools import cached_property
from typing import ClassVar

import more_itertools as mi
from typing_extensions import override


@functools.total_ordering
@dataclass(frozen=True)
class Hand:
    cards: str
    bid: int

    CARD_VALUES: ClassVar = "AKQJT98765432"[::-1]

    @functools.total_ordering
    @enum.unique
    class Type(enum.Enum):
        FIVE_OF_A_KIND = 7
        FOUR_OF_A_KIND = 6
        FULL_HOUSE = 5
        THREE_OF_A_KIND = 4
        TWO_PAIR = 3
        ONE_PAIR = 2
        HIGH_CARD = 1

        def __lt__(self, other: "Hand.Type") -> bool:
            return self.value < other.value

    def __lt__(self, other: "Hand") -> bool:
        return self._tuple_val() < other._tuple_val()

    def _tuple_val(self) -> tuple[Type, tuple[int, ...]]:
        return (self.type, tuple(self.CARD_VALUES.index(c) for c in self.cards))

    @cached_property
    def type(self) -> Type:
        counts = Counter(self.cards)
        return Hand._type_helper(counts)

    @staticmethod
    def _type_helper(counts: Counter[str]) -> Type:
        c = Counter(counts.values())
        if c[5] == 1:
            return Hand.Type.FIVE_OF_A_KIND
        if c[4] == 1:
            return Hand.Type.FOUR_OF_A_KIND
        if c[3] == 1:
            if c[2] == 1:
                return Hand.Type.FULL_HOUSE
            return Hand.Type.THREE_OF_A_KIND
        if c[2] == 2:
            return Hand.Type.TWO_PAIR
        if c[2] == 1:
            return Hand.Type.ONE_PAIR
        return Hand.Type.HIGH_CARD

    @classmethod
    def parse(cls, s: str) -> "Hand":
        cards, bid = s.split()
        return cls(cards, int(bid))


class HandB(Hand):
    CARD_VALUES: ClassVar = "AKQT98765432J"[::-1]

    @override
    @cached_property
    def type(self) -> Hand.Type:
        counts = Counter(self.cards)
        joker_count = counts.pop("J", 0)
        if joker_count == 0:
            return super().type
        if joker_count == 5:
            return Hand.Type.FIVE_OF_A_KIND
        k, _v = mi.one(counts.most_common(1))
        counts[k] += joker_count
        return self._type_helper(counts)


def parta(txt: str) -> int:
    hands = sorted(map(Hand.parse, txt.splitlines()))
    total_winnings = sum(h.bid * rank for rank, h in enumerate(hands, start=1))
    return total_winnings


def partb(txt: str) -> int:
    hands = sorted(map(HandB.parse, txt.splitlines()))
    total_winnings = sum(h.bid * rank for rank, h in enumerate(hands, start=1))
    return total_winnings


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
