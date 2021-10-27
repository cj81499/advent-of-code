from __future__ import annotations

import enum
from collections import defaultdict


class NodeState(enum.Enum):
    INFECTED = "#"
    CLEAN = "."
    WEAKENED = "W"
    FLAGGED = "F"


class VirusGrid:
    def __init__(self, grid: str):
        lines = grid.splitlines()
        self.grid = defaultdict(
            lambda: NodeState.CLEAN, {(x, y): NodeState(c) for y, line in enumerate(lines) for x, c in enumerate(line)}
        )
        self.dir = (0, -1)
        max_x = len(lines[0])
        max_y = len(lines)
        self.pos = (max_x // 2, max_y // 2)
        self.infection_count = 0

    @property
    def current_node(self):
        return self.grid[self.pos]

    @current_node.setter
    def current_node(self, new_state):
        self.grid[self.pos] = new_state

    def simulate(self, burst_count):
        for _ in range(burst_count):
            self.burst()

    def burst(self):
        dx, dy = self.dir
        if self.current_node == NodeState.INFECTED:
            self.dir = (-dy, dx)
            self.current_node = NodeState.CLEAN
        else:
            self.dir = (dy, -dx)
            self.current_node = NodeState.INFECTED
            self.infection_count += 1
        self._move()

    def _move(self):
        x, y = self.pos
        dx, dy = self.dir
        self.pos = (x + dx, y + dy)


class VirusGridB(VirusGrid):
    def burst(self):
        dx, dy = self.dir
        if self.current_node == NodeState.CLEAN:
            self.dir = (dy, -dx)
            self.current_node = NodeState.WEAKENED
        elif self.current_node == NodeState.WEAKENED:
            self.current_node = NodeState.INFECTED
            self.infection_count += 1
        elif self.current_node == NodeState.INFECTED:
            self.dir = (-dy, dx)
            self.current_node = NodeState.FLAGGED
        elif self.current_node == NodeState.FLAGGED:
            self.dir = (-dx, -dy)
            self.current_node = NodeState.CLEAN
        self._move()


def parta(txt: str, burst_count=10000):
    vg = VirusGrid(txt)
    vg.simulate(burst_count)
    return vg.infection_count


def partb(txt: str, burst_count=10000000):
    vg = VirusGridB(txt)
    vg.simulate(burst_count)
    return vg.infection_count


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
