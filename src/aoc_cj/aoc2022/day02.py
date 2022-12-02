import enum


class Move(enum.Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

    @staticmethod
    def parse(s: str) -> "Move":
        return {"X": Move.ROCK, "Y": Move.PAPER, "Z": Move.SCISSORS}[s]

    def score(self) -> int:
        return {Move.ROCK: 1, Move.PAPER: 2, Move.SCISSORS: 3}[self]

    def play(self, against: "Move") -> "Outcome":
        if self is against:
            return Outcome.DRAW
        return {
            Move.ROCK: {Move.PAPER: Outcome.LOSE, Move.SCISSORS: Outcome.WIN},
            Move.PAPER: {Move.ROCK: Outcome.WIN, Move.SCISSORS: Outcome.LOSE},
            Move.SCISSORS: {Move.ROCK: Outcome.LOSE, Move.PAPER: Outcome.WIN},
        }[self][against]


class Outcome(enum.Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"

    def score(self) -> int:
        return {Outcome.LOSE: 0, Outcome.DRAW: 3, Outcome.WIN: 6}[self]

    def my_move(self, against: "Move") -> "Move":
        if self is Outcome.DRAW:
            return against
        if self is Outcome.WIN:
            return {Move.ROCK: Move.PAPER, Move.PAPER: Move.SCISSORS, Move.SCISSORS: Move.ROCK}[against]
        # Outcome.LOSE
        return {Move.ROCK: Move.SCISSORS, Move.PAPER: Move.ROCK, Move.SCISSORS: Move.PAPER}[against]


def parta(txt: str) -> int:
    turns = ((Move(op_move), Move.parse(my_move)) for op_move, my_move in (line.split() for line in txt.splitlines()))
    return sum(my_move.score() + my_move.play(op_move).score() for op_move, my_move in turns)


def partb(txt: str) -> int:
    turns = ((Move(op_move), Outcome(outcome)) for op_move, outcome in (line.split() for line in txt.splitlines()))
    return sum(outcome.my_move(op_move).score() + outcome.score() for op_move, outcome in turns)


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
