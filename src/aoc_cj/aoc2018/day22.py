import dataclasses
import enum
import heapq
import itertools
from typing import Any


def adj(x, y):
    yield from ((x + dx, y + dy) for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)))


class Item(enum.Enum):
    NEITHER = 0
    TORCH = 1
    CLIMBING_GEAR = 2


@dataclasses.dataclass(frozen=True, eq=True, order=True)
class PrioritizedData:
    priority: int
    data: Any = dataclasses.field(compare=False)


@dataclasses.dataclass(frozen=True, eq=True)
class Node:
    pos: tuple[int, int]
    item: Item


class Type(enum.Enum):
    ROCKY = 0
    WET = 1
    NARROW = 2

    def __str__(self) -> str:
        return Type._STR_MAP[self]


Type._STR_MAP = {
    Type.ROCKY: ".",
    Type.NARROW: "|",
    Type.WET: "=",
}


class Region:
    def __init__(self, x, y, cave_system) -> None:
        self.x = x
        self.y = y
        self.cave_system = cave_system
        self.geologic_index = Region._geologic_index(x, y, cave_system)
        self.erosion_level = (self.geologic_index + cave_system.depth) % 20183
        self.type = Type(self.erosion_level % 3)

    @staticmethod
    def _geologic_index(x, y, cave_system):
        if (x, y) == CaveSystem.MOUTH:
            return 0
        if (x, y) == cave_system.target:
            return 0
        if y == 0:
            return x * 16807
        if x == 0:
            return y * 48271
        return cave_system.at(x - 1, y).erosion_level * cave_system.at(x, y - 1).erosion_level

    def risk_level(self):
        return self.type.value

    def can_use(self, item):
        return item.value != self.type.value

    def __str__(self) -> str:
        if (self.x, self.y) == CaveSystem.MOUTH:
            return "M"
        if (self.x, self.y) == self.cave_system.target:
            return "T"
        return str(self.type)


class CaveSystem:
    MOUTH = (0, 0)

    def __init__(self, depth, target) -> None:
        self.depth = depth
        self.target = target
        self.grid: dict[tuple[int, int], Region] = {}

    def at(self, x, y) -> Region:
        p = (x, y)
        if p not in self.grid:
            self.grid[p] = Region(x, y, self)
        return self.grid[p]

    @staticmethod
    def parse(cave_system: str):
        depth, target = (x.split(": ")[1] for x in cave_system.splitlines())
        target = tuple(map(int, target.split(",")))
        return CaveSystem(int(depth), target)

    def __str__(self, size=None) -> str:
        if size is None:
            size = (self.target[0] + 5, self.target[1] + 5)

        rows = []
        for y in range(size[1] + 1):
            row = []
            for x in range(size[0] + 1):
                row.append(str(self.at(x, y)))
            rows.append("".join(row))
        return "\n".join(rows)

    def risk_level(self):
        return sum(
            self.at(x, y).risk_level()
            for x, y in itertools.product(range(self.target[0] + 1), range(self.target[1] + 1))
        )

    def min_time_to_target(self):
        best_time: dict[Node, float] = {}
        time_to_target = float("inf")
        heap: list[PrioritizedData] = []

        node = PrioritizedData(0, Node(CaveSystem.MOUTH, Item.TORCH))
        heapq.heappush(heap, node)
        while node.priority < time_to_target:
            node = heapq.heappop(heap)
            # if we've been at this point with a lower time, we can't do better
            if node.priority < best_time.get(node.data, float("inf")):
                best_time[node.data] = node.priority
                if node.data.pos == self.target and node.data.item == Item.TORCH:
                    time_to_target = min(time_to_target, node.priority)
                for move in self.moves(node):
                    heapq.heappush(heap, move)

        return time_to_target

    def moves(self, move: PrioritizedData):
        # move by switching items
        region = self.at(*move.data.pos)
        can_switch_to = next(filter(lambda i: i != move.data.item and region.can_use(i), Item))
        yield PrioritizedData(move.priority + 7, Node(move.data.pos, can_switch_to))

        # move by changing positions
        for new_pos in adj(*move.data.pos):
            # if we can move to the location without changing items
            if all(n >= 0 for n in new_pos) and self.at(*new_pos).can_use(move.data.item):
                yield PrioritizedData(move.priority + 1, Node(new_pos, move.data.item))


def part_1(txt):
    cave_system = CaveSystem.parse(txt)
    return cave_system.risk_level()


def part_2(txt):
    cave_system = CaveSystem.parse(txt)
    return cave_system.min_time_to_target()


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
