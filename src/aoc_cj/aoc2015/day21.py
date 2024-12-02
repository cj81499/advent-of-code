import itertools
import re
from collections.abc import Generator
from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    cost: int
    damage: int
    armor: int

    # split on 2 or more spaces
    _PARSE_REGEX = re.compile(r"  +")

    @staticmethod
    def parse(item: str) -> "Item":
        name, *stats = re.split(Item._PARSE_REGEX, item)
        return Item(name, *map(int, stats))


SHOP = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
""".strip()

WEAPONS, ARMOR, RINGS = SHOP.split("\n\n")
WEAPONS = {Item.parse(line) for line in WEAPONS.splitlines()[1:]}
# add None b/c armor and rings are optional
ARMOR = {None, *(Item.parse(line) for line in ARMOR.splitlines()[1:])}
RINGS = {None, *(Item.parse(line) for line in RINGS.splitlines()[1:])}


def go_shopping(gold: float) -> Generator[tuple[Item, ...], None, None]:
    for purchase in itertools.product(WEAPONS, ARMOR, RINGS, RINGS):
        # remove None, since we can't purchase nothingness
        purchase_no_none = tuple(i for i in purchase if i is not None)
        # can't purchase same item more than once (each item must be unique)
        if len(set(purchase_no_none)) == len(purchase_no_none):
            cost = sum(i.cost for i in purchase_no_none)
            if cost <= gold:
                yield purchase_no_none


@dataclass
class Unit:
    hit_points: int
    damage: int
    armor: int

    def attack(self, other: "Unit") -> None:
        other.hit_points -= max(1, self.damage - other.armor)

    def is_alive(self) -> bool:
        return self.hit_points > 0

    def copy(self) -> "Unit":
        return Unit(self.hit_points, self.damage, self.armor)

    def equip(self, item: Item) -> None:
        self.damage += item.damage
        self.armor += item.armor

    @staticmethod
    def parse(unit: str) -> "Unit":
        data = map(int, (line.split(": ")[1] for line in unit.splitlines()))
        return Unit(*data)


def battle(player: Unit, boss: Unit) -> Unit:
    active, inactive = player, boss
    while player.is_alive() and boss.is_alive():
        active.attack(inactive)
        active, inactive = inactive, active
    return player if player.is_alive() else boss


def part_1(txt: str) -> int:
    boss = Unit.parse(txt)
    for gold in itertools.count():
        for purchase in go_shopping(gold):
            player = Unit(100, 0, 0)
            for item in purchase:
                player.equip(item)

            winner = battle(player, boss.copy())
            if winner is player:
                return gold
    raise ValueError


def part_2(txt: str) -> int:
    boss = Unit.parse(txt)
    most_expensive_loss = 0
    for purchase in go_shopping(float("inf")):
        player = Unit(100, 0, 0)
        for item in purchase:
            player.equip(item)

        winner = battle(player, boss.copy())
        if winner is not player:
            most_expensive_loss = max(most_expensive_loss, sum(i.cost for i in purchase))
    return most_expensive_loss


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
