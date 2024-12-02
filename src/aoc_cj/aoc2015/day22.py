from dataclasses import dataclass, replace
from functools import cache


@dataclass(frozen=True)
class Spell:
    name: str
    cost: int
    damage: int = 0
    healing: int = 0
    armor: int = 0
    mana: int = 0
    duration: int = 1


SPELLS = [
    Spell("Magic Missile", 53, damage=4),
    Spell("Drain", 73, damage=2, healing=2),
    Spell("Shield", 113, duration=6, armor=7),
    Spell("Poison", 173, duration=6, damage=3),
    Spell("Recharge", 229, duration=5, mana=101),
]

# in practice, trying expensive spells first is slightly faster
# I think this is because we can start skipping (see line 90) sooner.
SPELLS.reverse()


@dataclass(frozen=True)
class Unit:
    name: str
    hit_points: int
    damage: int = 0
    armor: int = 0
    mana: int = 0

    def is_dead(self):
        return self.hit_points <= 0

    @staticmethod
    def parse(unit: str, name: str):
        data = {k.lower().replace(" ", "_"): int(v) for k, v in (line.split(": ") for line in unit.splitlines())}
        return Unit(name, **data)


def castable_spells(player: Unit, effects):
    yield from (s for s in SPELLS if s.name not in (e.name for e in effects) and s.cost <= player.mana)


def after_effects(player: Unit, boss: Unit, effects):
    new_effects = set()
    damage = 0
    healing = 0
    armor = 0
    mana = 0
    for e in effects:
        damage += e.damage
        healing += e.healing
        armor += e.armor
        mana += e.mana
        if e.duration - 1 > 0:
            new_effects.add(replace(e, duration=e.duration - 1))
    new_player = replace(player, hit_points=player.hit_points + healing, armor=armor, mana=player.mana + mana)
    new_boss = replace(boss, hit_points=boss.hit_points - damage)
    return new_player, new_boss, frozenset(new_effects)


# @cache
@cache
def min_mana_for_player_win_player_turn(player: Unit, boss: Unit, effects, cost_so_far, best_so_far, hard=False):
    # lose 1 hp in hard mode
    if hard:
        player = replace(player, hit_points=player.hit_points - 1)
        if player.is_dead():
            return float("inf")
    # effects
    player, boss, effects = after_effects(player, boss, effects)
    # check for boss death
    if boss.is_dead():
        return cost_so_far
    # cast spell
    for spell in castable_spells(player, effects):
        cost = spell.cost + cost_so_far
        # if we've already found a cheaper solution, don't waste time with a more expensive one
        if cost > best_so_far:
            continue
        new_player = replace(player, mana=player.mana - spell.cost)
        new_effects = effects.union({spell})
        best_so_far = min(
            best_so_far, min_mana_for_player_win_boss_turn(new_player, boss, new_effects, cost, best_so_far, hard=hard)
        )
    return best_so_far


@cache
def min_mana_for_player_win_boss_turn(player: Unit, boss: Unit, effects, cost_so_far, best_so_far, hard=False):
    # effects
    player, boss, effects = after_effects(player, boss, effects)
    # check for boss death
    if boss.is_dead():
        return cost_so_far
    # deal damage
    player = replace(player, hit_points=player.hit_points - max(1, boss.damage - player.armor))
    # check for player death
    if player.is_dead():
        return float("inf")
    return min_mana_for_player_win_player_turn(player, boss, effects, cost_so_far, best_so_far, hard=hard)


def min_mana_for_player_win(player: Unit, boss: Unit, hard=False):
    return min_mana_for_player_win_player_turn(player, boss, frozenset(), 0, float("inf"), hard=hard)


DEFAULT_PLAYER_HP = 50
DEFAULT_PLAYER_MANA = 500


def part_1(txt, player_hp=DEFAULT_PLAYER_HP, player_mana=DEFAULT_PLAYER_MANA):
    boss = Unit.parse(txt, "Boss")
    player = Unit("Player", player_hp, mana=player_mana)

    return min_mana_for_player_win(player, boss)


def part_2(txt):
    boss = Unit.parse(txt, "Boss")
    player = Unit("Player", DEFAULT_PLAYER_HP, mana=DEFAULT_PLAYER_MANA)

    return min_mana_for_player_win(player, boss, hard=True)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
