import functools
import itertools
from collections import deque
from collections.abc import Generator

UP = -1j
DOWN = 1j
LEFT = -1
RIGHT = 1


import dataclasses


@dataclasses.dataclass(frozen=True)
class Grid:
    contents: dict[complex, str]

    @functools.cached_property
    def max_x(self) -> int:
        return int(max(p.real for p in self.contents))

    @functools.cached_property
    def max_y(self) -> int:
        return int(max(p.imag for p in self.contents))

    def __contains__(self, item: "LightBeam") -> bool:
        return item.pos in self.contents

    def __getitem__(self, key: "LightBeam") -> str:
        return self.contents[key.pos]

    @staticmethod
    def parse(s: str) -> "Grid":
        return Grid({complex(x, y): c for y, line in enumerate(s.splitlines()) for x, c in enumerate(line)})

    def energized_tiles(self, start: "LightBeam") -> frozenset[complex]:
        seen = set[LightBeam]()
        to_explore = deque((start,))
        while to_explore:
            light = to_explore.popleft()
            if light in seen or light not in self:
                continue
            seen.add(light)
            to_explore.extend(light.advance(self[light]))
        return frozenset(l.pos for l in seen)


import dataclasses


@dataclasses.dataclass(frozen=True)
class LightBeam:
    pos: complex
    direction: complex

    @functools.cache
    def advance(self, contents: str) -> frozenset["LightBeam"]:
        return frozenset(self._advance(contents))

    def _advance(self, contents: str) -> Generator["LightBeam"]:
        if contents == "-" and self.direction in (UP, DOWN):
            yield LightBeam(self.pos + LEFT, LEFT)
            yield LightBeam(self.pos + RIGHT, RIGHT)
        elif contents == "|" and self.direction in (LEFT, RIGHT):
            yield LightBeam(self.pos + UP, UP)
            yield LightBeam(self.pos + DOWN, DOWN)
        elif contents == "/":
            new_direction = {UP: RIGHT, DOWN: LEFT, LEFT: DOWN, RIGHT: UP}[self.direction]
            yield LightBeam(self.pos + new_direction, new_direction)
        elif contents == "\\":
            new_direction = {UP: LEFT, DOWN: RIGHT, LEFT: UP, RIGHT: DOWN}[self.direction]
            yield LightBeam(self.pos + new_direction, new_direction)
        else:
            yield LightBeam(self.pos + self.direction, self.direction)


def part_1(txt: str) -> int:
    return len(Grid.parse(txt).energized_tiles(LightBeam(0, 1)))


def part_2(txt: str) -> int:
    grid = Grid.parse(txt)
    initial_configurations = itertools.chain(
        (LightBeam(complex(0, y), 1) for y in range(grid.max_y + 1)),  # start from left side
        (LightBeam(complex(grid.max_x, y), -1) for y in range(grid.max_y + 1)),  # start from right side
        (LightBeam(complex(x, 0), 1j) for x in range(grid.max_x + 1)),  # start from top side
        (LightBeam(complex(x, grid.max_y), -1j) for x in range(grid.max_x + 1)),  # start from bottom side
    )
    return max(len(grid.energized_tiles(l)) for l in initial_configurations)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
