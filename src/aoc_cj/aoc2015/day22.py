import dataclasses
import functools
from collections.abc import Generator


@dataclasses.dataclass(frozen=True)
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


@dataclasses.dataclass(frozen=True)
class Unit:
    name: str
    hit_points: int
    damage: int = 0
    armor: int = 0
    mana: int = 0

    def is_dead(self) -> bool:
        return self.hit_points <= 0

    @staticmethod
    def parse(unit: str, name: str) -> "Unit":
        data = {k.lower().replace(" ", "_"): int(v) for k, v in (line.split(": ") for line in unit.splitlines())}
        return Unit(name, **data)


def castable_spells(player: Unit, effects: frozenset[Spell]) -> Generator[Spell]:
    yield from (s for s in SPELLS if s.name not in (e.name for e in effects) and s.cost <= player.mana)


def after_effects(player: Unit, boss: Unit, effects: frozenset[Spell]) -> tuple[Unit, Unit, frozenset[Spell]]:
    new_effects = set[Spell]()
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
            new_effects.add(dataclasses.replace(e, duration=e.duration - 1))
    new_player = dataclasses.replace(
        player, hit_points=player.hit_points + healing, armor=armor, mana=player.mana + mana
    )
    new_boss = dataclasses.replace(boss, hit_points=boss.hit_points - damage)
    return new_player, new_boss, frozenset(new_effects)


@functools.cache
def min_mana_for_player_win_player_turn(
    player: Unit,
    boss: Unit,
    effects: frozenset[Spell],
    cost_so_far: int,
    best_so_far: int | None,
    *,
    hard: bool = False,
) -> int | None:
    # lose 1 hp in hard mode
    if hard:
        player = dataclasses.replace(player, hit_points=player.hit_points - 1)
        if player.is_dead():
            return None
    # effects
    player, boss, effects = after_effects(player, boss, effects)
    # check for boss death
    if boss.is_dead():
        return cost_so_far
    # cast spell
    for spell in castable_spells(player, effects):
        cost = spell.cost + cost_so_far
        # if we've already found a cheaper solution, don't waste time with a more expensive one
        if best_so_far is not None and cost > best_so_far:
            continue
        new_player = dataclasses.replace(player, mana=player.mana - spell.cost)
        new_effects = effects.union({spell})
        min_mana = min_mana_for_player_win_boss_turn(new_player, boss, new_effects, cost, best_so_far, hard=hard)
        if min_mana is not None and (best_so_far is None or min_mana < best_so_far):
            best_so_far = min_mana
    return best_so_far


@functools.cache
def min_mana_for_player_win_boss_turn(
    player: Unit,
    boss: Unit,
    effects: frozenset[Spell],
    cost_so_far: int,
    best_so_far: int,
    *,
    hard: bool = False,
) -> int | None:
    # effects
    player, boss, effects = after_effects(player, boss, effects)
    # check for boss death
    if boss.is_dead():
        return cost_so_far
    # deal damage
    player = dataclasses.replace(player, hit_points=player.hit_points - max(1, boss.damage - player.armor))
    # check for player death
    if player.is_dead():
        return None
    return min_mana_for_player_win_player_turn(player, boss, effects, cost_so_far, best_so_far, hard=hard)


def min_mana_for_player_win(player: Unit, boss: Unit, *, hard: bool = False) -> int:
    min_mana = min_mana_for_player_win_player_turn(player, boss, frozenset(), 0, None, hard=hard)
    if min_mana is None:
        raise ValueError
    return min_mana


DEFAULT_PLAYER_HP = 50
DEFAULT_PLAYER_MANA = 500


def part_1(txt: str, *, player_hp: int = DEFAULT_PLAYER_HP, player_mana: int = DEFAULT_PLAYER_MANA) -> int:
    boss = Unit.parse(txt, "Boss")
    player = Unit("Player", player_hp, mana=player_mana)

    return min_mana_for_player_win(player, boss)


def part_2(txt: str) -> int:
    boss = Unit.parse(txt, "Boss")
    player = Unit("Player", DEFAULT_PLAYER_HP, mana=DEFAULT_PLAYER_MANA)

    return min_mana_for_player_win(player, boss, hard=True)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
