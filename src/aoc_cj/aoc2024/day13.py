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

    # using linear algebra solution, but still neat!
    def cheapest_way_to_win(self, off_by: int = 0) -> int | None:  # pragma: no cover
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

    def cheapest_way_to_win_lin_alg(self, off_by: int = 0) -> int | None:
        # Solve system of 2 linear equations where (px, py) is prize position, (ax, ay)/(bx, by) is movement from pressing a/b.
        #   px = ax * a + bx * b  # noqa: ERA001
        #   py = ay * a + by * b  # noqa: ERA001
        px, py = self.prize
        px += off_by
        py += off_by
        ax, ay = self.a
        bx, by = self.b

        # determinant of the coefficient matrix
        det = ax * by - ay * bx

        # if det == 0, there's no solution
        if det == 0:  # pragma: no cover - not relevant for our input
            return 0

        # solve for a and b
        a_float = (px * by - bx * py) / det
        b_float = (ax * py - ay * px) / det

        # if the solution does not use an integer number of button presses, there's no solution
        if (a := int(a_float)) != a_float or (b := int(b_float)) != b_float:
            return 0

        # return the cost to get the prize
        return 3 * a + b


def part_1(txt: str) -> int:
    return solve(txt)


def part_2(txt: str) -> int:
    return solve(txt, off_by=10_000_000_000_000)  # pragma: no cover - no test cases


def solve(txt: str, off_by: int = 0) -> int:
    return sum(g.cheapest_way_to_win_lin_alg(off_by=off_by) or 0 for g in map(Game.parse, txt.split("\n\n")))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
