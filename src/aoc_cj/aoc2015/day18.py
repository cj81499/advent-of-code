import contextlib
import enum
from collections import Counter
from collections.abc import Generator
from typing import assert_never

import more_itertools as mi


class LightState(enum.StrEnum):
    ON = "#"
    OFF = "."


LightshowState = list[list[LightState]]


def parse_lightshow_state(txt: str) -> LightshowState:
    return [[LightState(c) for c in line] for line in txt.splitlines()]


def lightshow(initial_state: str, *, corners_stuck_on: bool = False) -> Generator[LightshowState]:
    state = parse_lightshow_state(initial_state)
    while True:
        if corners_stuck_on:
            state[0][0] = LightState.ON
            state[0][-1] = LightState.ON
            state[-1][0] = LightState.ON
            state[-1][-1] = LightState.ON
        yield state
        new_state = []
        for y, row in enumerate(state):
            new_row = []
            for x, initial_light_state in enumerate(row):
                neighbor_counts = Counter(neighbor_values(state, x, y))
                if initial_light_state == LightState.ON:
                    light_state = LightState.ON if neighbor_counts[LightState.ON] in (2, 3) else LightState.OFF
                elif initial_light_state == LightState.OFF:
                    light_state = LightState.ON if neighbor_counts[LightState.ON] == 3 else LightState.OFF
                else:
                    assert_never(initial_light_state)
                new_row.append(light_state)
            new_state.append(new_row)
        state = new_state


def neighbor_values(grid: LightshowState, x: int, y: int) -> Generator[LightState]:
    neighbors = (
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    )
    for nx, ny in neighbors:
        if nx >= 0 and ny >= 0:
            with contextlib.suppress(IndexError):
                yield grid[ny][nx]


def part_1(txt: str, *, steps: int = 100) -> int:
    return _solve(txt, steps)


def part_2(txt: str, *, steps: int = 100) -> int:
    return _solve(txt, steps, corners_stuck_on=True)


def _solve(txt: str, steps: int, *, corners_stuck_on: bool = False) -> int:
    lightshow_simulation = lightshow(txt, corners_stuck_on=corners_stuck_on)
    end_state = mi.nth(lightshow_simulation, steps)
    assert end_state is not None
    return sum(sum(1 for c in row if c == LightState.ON) for row in end_state)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
