import dataclasses
import itertools
from functools import cache
from typing import Iterator

from more_itertools import pairwise, take


@dataclasses.dataclass
class Player:
    position: int
    score: int = 0

    def turn(self, die: Iterator[int]):
        rolls = take(3, die)
        self.position = (self.position - 1 + sum(rolls)) % 10 + 1
        self.score += self.position


def parta(txt: str) -> int:
    die = ((n % 100) + 1 for n in itertools.count())
    players = [Player(int(line.split()[-1])) for line in txt.splitlines()]
    roll_count = 0
    for active_player, inactive_player in pairwise(itertools.cycle(players)):
        active_player.turn(die)
        roll_count += 3
        if active_player.score >= 1000:
            return inactive_player.score * roll_count


@dataclasses.dataclass(frozen=True)
class State:
    active_pos: int
    active_score: int
    inactive_pos: int
    inactive_score: int
    active: int = 0


@cache
def helper(state: State):
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


def partb(txt: str) -> None:
    players = [Player(int(line.split()[-1])) for line in txt.splitlines()]
    state = State(
        players[0].position,
        0,
        players[1].position,
        0,
        0,
    )

    return max(helper(state))


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
