import dataclasses

import z3  # type: ignore[import-untyped]

from aoc_cj import util


@dataclasses.dataclass
class Game:
    a: tuple[int, int]
    b: tuple[int, int]
    prize: tuple[int, int]

    @staticmethod
    def parse(txt: str) -> "Game":
        a, b, prize = map(tuple, map(util.ints, txt.splitlines()))
        assert len(a) == 2
        assert len(b) == 2
        assert len(prize) == 2
        return Game(a=a, b=b, prize=prize)

    def cheapest_way_to_win(self, off_by: int = 0) -> int | None:
        # create an optimization problem
        opt = z3.Optimize()

        # describe the game to the optimizer
        a_presses, b_presses, cost = z3.Ints(("a_presses", "b_presses", "cost"))

        x = self.a[0] * a_presses + self.b[0] * b_presses
        y = self.a[1] * a_presses + self.b[1] * b_presses

        opt.add(x == self.prize[0] + off_by)
        opt.add(y == self.prize[1] + off_by)
        opt.add(cost == a_presses * 3 + b_presses)

        # minimize cost to reach the prize
        opt.minimize(cost)

        # if there's no way to win the prize
        if opt.check() != z3.sat:
            return None

        # return the minimal cost to win the prize
        model = opt.model()
        return int(model[cost].as_long())


def part_1(txt: str) -> int:
    return solve(txt)


def part_2(txt: str) -> int:
    return solve(txt, off_by=10_000_000_000_000)


def solve(txt: str, off_by: int = 0) -> int:
    return sum(g.cheapest_way_to_win(off_by=off_by) or 0 for g in map(Game.parse, txt.split("\n\n")))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
