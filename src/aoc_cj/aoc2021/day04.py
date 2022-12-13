from collections.abc import Iterator
from itertools import chain


class Board:
    def __init__(self, grid: list[list[int]]):
        self._grid = grid
        self._marks = [[False for _ in row] for row in grid]
        self._last_draw: int = -1

    def mark_number(self, draw: int) -> None:
        if self.is_won():
            raise ValueError("cannot mark number after game is won")
        self._last_draw = draw
        for i, row in enumerate(self._grid):
            for j, n in enumerate(row):
                if n == draw:
                    self._marks[i][j] = True

    def is_won(self) -> bool:
        return any(all(marks) for marks in self._marks) or any(all(marks) for marks in zip(*self._marks))

    def score(self) -> int:
        if not self.is_won():
            raise ValueError("cannot get score until game is won")
        unmarked_numbers = (n for n, marked in zip(chain(*self._grid), chain(*self._marks)) if not marked)
        return sum(unmarked_numbers) * self._last_draw

    @staticmethod
    def parse(txt: str) -> "Board":
        return Board([[int(n) for n in line.split()] for line in txt.splitlines()])


def winners(draws: list[int], boards: list[Board]) -> Iterator[Board]:
    for n in draws:
        for b in (b for b in boards if not b.is_won()):
            b.mark_number(n)
            if b.is_won():
                yield b


def parse(txt: str) -> tuple[list[int], list[Board]]:
    draws, *boards = txt.split("\n\n")
    return [int(x) for x in draws.split(",")], [Board.parse(b) for b in boards]


def parta(txt: str) -> int:
    draws, boards = parse(txt)
    first_winner = next(winners(draws, boards))
    return first_winner.score()


def partb(txt: str) -> int:
    draws, boards = parse(txt)
    *_rest, last_winner = winners(draws, boards)
    return last_winner.score()


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
