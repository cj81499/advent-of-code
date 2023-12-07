import dataclasses
import enum
import functools
from collections import Counter
from functools import cached_property

CARD_VALUES = "AKQJT98765432"[::-1]


@functools.total_ordering
@dataclasses.dataclass(frozen=True)  # TODO: add dataclasses to auto imports
class Hand:
    cards: str
    bid: int

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
        return (self.type, tuple(CARD_VALUES.index(c) for c in self.cards))

    @cached_property
    def type(self) -> Type:
        counts = Counter(self.cards)
        counts2 = Counter(counts.values())
        if counts2[5] == 1:
            return Hand.Type.FIVE_OF_A_KIND
        if counts2[4] == 1:
            return Hand.Type.FOUR_OF_A_KIND
        if counts2[3] == 1:
            if counts2[2] == 1:
                return Hand.Type.FULL_HOUSE
            return Hand.Type.THREE_OF_A_KIND
        if counts2[2] == 2:
            return Hand.Type.TWO_PAIR
        if counts2[2] == 1:
            return Hand.Type.ONE_PAIR
        return Hand.Type.HIGH_CARD

    @staticmethod
    def parse(s: str) -> "Hand":
        cards, bid = s.split()
        return Hand(cards, int(bid))


def parta(txt: str) -> int:
    hands = sorted(map(Hand.parse, txt.splitlines()))
    total_winnings = sum(h.bid * rank for rank, h in enumerate(hands, start=1))
    return total_winnings


def partb(txt: str) -> int:
    raise NotImplementedError()


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
