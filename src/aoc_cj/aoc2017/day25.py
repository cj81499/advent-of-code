import dataclasses
from collections import defaultdict


@dataclasses.dataclass
class State:
    letter: str
    write_value: tuple[int, int]
    move: tuple[int, int]
    next_state: tuple[str, str]

    @staticmethod
    def parse(state: str) -> "State":
        lines = state.splitlines()
        assert len(lines) == 9
        letter = lines[0][-2]
        write_values = tuple(int(line[-2]) for line in (lines[2], lines[6]))
        assert len(write_values) == 2
        moves = tuple(1 if line.endswith("right.") else -1 for line in (lines[3], lines[7]))
        assert len(moves) == 2
        next_states = tuple(line[-2] for line in (lines[4], lines[8]))
        assert len(next_states) == 2
        return State(letter, write_values, moves, next_states)


class TurningMachine:
    def __init__(self, start_state: str, states: list[State]):
        self._tape = defaultdict[int, int](int)
        self._states = {s.letter: s for s in states}
        self._state = self._states[start_state]
        self._cursor = 0

    def step(self) -> None:
        current_val = self._tape[self._cursor]
        self._tape[self._cursor] = self._state.write_value[current_val]
        self._cursor += self._state.move[current_val]
        self._state = self._states[self._state.next_state[current_val]]

    def run(self, steps: int) -> None:
        for _ in range(steps):
            self.step()

    def checksum(self) -> int:
        return sum(self._tape.values())


def part_1(txt: str) -> int:
    info, *states = txt.split("\n\n")
    start_state, checksum_steps = info.splitlines()
    start_state = start_state[-2]
    checksum_steps = int(checksum_steps.split()[-2])
    states = [State.parse(s) for s in states]
    tm = TurningMachine(start_state, states)
    tm.run(checksum_steps)
    return tm.checksum()


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
