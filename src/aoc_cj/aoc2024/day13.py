import dataclasses
import itertools

import z3

from aoc_cj.util import ints

_CONVERSION_ERROR = 10_000_000_000_000


@dataclasses.dataclass
class Game:
    a: tuple[int, int]
    b: tuple[int, int]
    prize: tuple[int, int]

    @staticmethod
    def parse(txt: str) -> "Game":
        a, b, prize = txt.splitlines()
        return Game(
            a=tuple(ints(a)),
            b=tuple(ints(b)),
            prize=tuple(ints(prize)),
        )

    def cheapest_way_to_win(self) -> int | None:
        min_cost: int | None = None
        for a_presses, b_presses in itertools.product(range(100), range(100)):
            end_pos = (self.a[0] * a_presses + self.b[0] * b_presses, self.a[1] * a_presses + self.b[1] * b_presses)
            if end_pos == self.prize:
                cost = a_presses * 3 + b_presses
                min_cost = cost if min_cost is None else min(cost, min_cost)
        return min_cost

    def cheapest_way_to_win2(self) -> int | None:
        a_presses = z3.Int("a_presses")
        b_presses = z3.Int("b_presses")

        end_x = self.a[0] * a_presses + self.b[0] * b_presses
        end_y = self.a[1] * a_presses + self.b[1] * b_presses

        cost = z3.Int("cost")

        opt = z3.Optimize()
        opt.add(end_x == self.prize[0] + _CONVERSION_ERROR)
        opt.add(end_y == self.prize[1] + _CONVERSION_ERROR)
        opt.add(cost == a_presses * 3 + b_presses)
        opt.minimize(cost)

        # solve the problem
        is_sat = opt.check()
        if is_sat != z3.sat:
            return None
        model = opt.model()
        return int(model[cost].as_long())


def part_1(txt: str) -> int:
    games = list(map(Game.parse, txt.split("\n\n")))
    return sum(g.cheapest_way_to_win() or 0 for g in games)


def part_2(txt: str) -> int:
    games = list(map(Game.parse, txt.split("\n\n")))
    return sum(g.cheapest_way_to_win2() or 0 for g in games)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
