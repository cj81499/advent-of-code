import dataclasses
import itertools
from collections.abc import Iterator
from functools import cache

import more_itertools as mi


@dataclasses.dataclass
class Player:
    position: int
    score: int = 0

    def turn(self, die: Iterator[int]) -> None:
        rolls = mi.take(3, die)
        self.position = (self.position - 1 + sum(rolls)) % 10 + 1
        self.score += self.position


def part_1(txt: str) -> int:
    die = ((n % 100) + 1 for n in itertools.count())
    players = [Player(int(line.split()[-1])) for line in txt.splitlines()]
    roll_count = 0
    for active_player, inactive_player in itertools.pairwise(itertools.cycle(players)):
        active_player.turn(die)
        roll_count += 3
        if active_player.score >= 1000:
            return inactive_player.score * roll_count
    assert False, "unreachable"


@dataclasses.dataclass(frozen=True)
class State:
    active_pos: int
    active_score: int
    inactive_pos: int
    inactive_score: int
    active: int = 0


@cache
def helper(state: State) -> list[int]:
    wins = [0, 0]
    possible_rolls = itertools.product(range(1, 4), range(1, 4), range(1, 4))
    for rolls in possible_rolls:
        new_pos = (state.active_pos - 1 + sum(rolls)) % 10 + 1
        new_score = state.active_score + new_pos
        if new_score >= 21:
            wins[state.active] += 1
        else:
            next_state = State(
                state.inactive_pos,
                state.inactive_score,
                new_pos,
                new_score,
                (state.active + 1) % 2,
            )
            result = helper(next_state)
            wins[0] += result[0]
            wins[1] += result[1]
    return wins


def part_2(txt: str) -> int:
    players = [Player(int(line.split()[-1])) for line in txt.splitlines()]
    state = State(players[0].position, 0, players[1].position, 0, 0)

    return max(helper(state))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
