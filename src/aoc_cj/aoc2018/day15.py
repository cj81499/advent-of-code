import dataclasses
import itertools
from collections import deque
from enum import Enum


class Node:
    def __init__(self, to: "Location"):
        self.to = to

    def adjacent_nodes(self):
        return [MoveNode(self, d) for d in Direction]


class StartNode(Node):
    def __init__(self, start: "Location"):
        super().__init__(start)


class MoveNode(Node):
    def __init__(self, from_: Node, direction: "Direction"):
        super().__init__(from_.to.add(direction))
        self.from_ = from_
        self.direction = direction

    def move_direction(self):
        if isinstance(self.from_, MoveNode):
            return self.from_.move_direction()
        return self.direction

    def path(self) -> list:
        if isinstance(self.from_, MoveNode):
            return self.from_.path().append(self.direction)
        return [self.direction]


class NoTargetsFoundException(Exception):
    pass


@dataclasses.dataclass(frozen=True, eq=True)
class Location:
    x: int
    y: int

    def add(self, other):
        if isinstance(other, Direction):
            other = other.value
        return Location(self.x + other.x, self.y + other.y)

    def adjacent_locations(self):
        return [self.add(d) for d in Direction]


class Direction(Enum):
    UP = Location(0, -1)
    LEFT = Location(-1, 0)
    RIGHT = Location(+1, 0)
    DOWN = Location(0, +1)


@dataclasses.dataclass
class CavePiece:
    cave_string: str
    cave: "Cave"
    loc: Location

    def __str__(self):
        return self.cave_string


class Wall(CavePiece):
    def __init__(self, cave: "Cave", loc: Location):
        super().__init__("#", cave, loc)


class Open(CavePiece):
    def __init__(self, cave: "Cave", loc: Location):
        super().__init__(".", cave, loc)


class Unit(CavePiece):
    DEFAULT_ATTACK_POWER = 3
    DEFAULT_HIT_POINTS = 200

    def __init__(self, board_string: str, cave: "Cave", loc: Location, attack_power: int = DEFAULT_ATTACK_POWER):
        super().__init__(board_string, cave, loc)
        self.attack_power = attack_power
        self.hit_points = Unit.DEFAULT_HIT_POINTS

    def deal_damage(self, other: "Unit"):
        other.hit_points -= self.attack_power
        if other.is_dead():
            other.die()

    def is_dead(self):
        return self.hit_points <= 0

    def is_alive(self):
        return self.hit_points > 0

    def die(self):
        self.cave.remove_unit_at(self.loc)

    def turn(self):
        assert self.cave.at(self.loc) == self

        # Each unit begins its turn by identifying all possible targets (Target units).
        targets = self.get_targets()
        # If no targets remain, combat ends.
        if len(targets) == 0:
            raise NoTargetsFoundException()

        # Then, the unit identifies all of the open squares (.) that are in range of
        # each target; these are the squares which are adjacent (immediately up, down,
        # left, or right) to any target and which aren't already occupied by a wall or
        # another unit.
        in_range_locations = {loc for t in targets for loc in t.loc.adjacent_locations()}

        in_range_open_locations = {loc for loc in in_range_locations if isinstance(self.cave.at(loc), Open)}

        # If the unit is not already in range of a target, and there are no open
        # squares which are in range of a target, the unit ends its turn.
        in_range_of_target = self.in_range_of_target()
        if not in_range_of_target and len(in_range_open_locations) == 0:
            return

        # If the unit is already in range of a target, it does not move, but continues
        # its turn with an attack. Otherwise, since it is not in range of a target, it
        # moves.
        if not in_range_of_target:
            self.move(in_range_open_locations)

        # if there's something to attack, attack it!
        if self.in_range_of_target():
            self.attack()

    def move(self, in_range: set[Location]):
        to_explore = deque(StartNode(self.loc).adjacent_nodes())
        explored = set()

        selected_move_node = None
        while len(to_explore) > 0:
            move_node = to_explore.popleft()
            if move_node.to not in explored:
                if isinstance(self.cave.at(move_node.to), Open):
                    if move_node.to in in_range:
                        selected_move_node = move_node
                        break
                    to_explore.extend(move_node.adjacent_nodes())
                explored.add(move_node.to)

        if selected_move_node is not None:
            self.cave.move_unit(self.loc, selected_move_node.move_direction())

    def attack(self):
        min_hp = float("inf")
        min_hp_targets = []
        for target in self.adjacent_targets():
            if target.hit_points <= min_hp:
                if target.hit_points < min_hp:
                    min_hp = target.hit_points
                    min_hp_targets.clear()
                min_hp_targets.append(target)
        selected_target = min_hp_targets[0]
        self.deal_damage(selected_target)

    def in_range_of_target(self):
        return len(self.adjacent_targets()) != 0

    def adjacent_targets(self):
        adj_cps = (self.cave.at(loc) for loc in self.loc.adjacent_locations())
        return [cp for cp in adj_cps if self.is_target(cp)]

    def is_target(self, other: CavePiece):
        return isinstance(other, Unit) and self.cave_string != other.cave_string

    def get_targets(self):
        targets = []
        for y in range(self.cave.height):
            for x in range(self.cave.width):
                cp = self.cave.at(Location(x, y))
                if self.is_target(cp):
                    targets.append(cp)
        return targets


class Goblin(Unit):
    def __init__(self, cave: "Cave", loc: Location):
        super().__init__("G", cave, loc)


class Elf(Unit):
    def __init__(self, cave: "Cave", loc: Location, attack_power: int):
        super().__init__("E", cave, loc, attack_power)


class CavePieceFactory:
    def __init__(self, elf_attack_power: int):
        self.elf_attack_power = elf_attack_power

    def get_cave_piece(self, c: str, cave: "Cave", loc: Location):
        if c == "#":
            return Wall(cave, loc)
        elif c == "G":
            return Goblin(cave, loc)
        elif c == "E":
            return Elf(cave, loc, self.elf_attack_power)
        return Open(cave, loc)


class Cave:
    def __init__(self, txt: str, elf_attack_power: int = Unit.DEFAULT_ATTACK_POWER):
        self._rep = {}
        lines = txt.splitlines()
        self.height = len(lines)
        self.width = len(lines[0])
        bpf = CavePieceFactory(elf_attack_power)
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                loc = Location(x, y)
                piece = bpf.get_cave_piece(c, self, loc)
                self._rep[loc] = piece

    def __str__(self):
        rows = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                loc = Location(x, y)
                cp = self.at(loc)
                row.append(str(cp))
            rows.append("".join(row))
        return "\n".join(rows)

    def move_unit(self, src: Location, direction: Direction):
        unit = self.at(src)
        assert isinstance(unit, Unit)
        destination = src.add(direction)
        destination_cave_piece = self.at(destination)
        assert isinstance(destination_cave_piece, Open)
        self._rep[destination] = unit
        self._rep[src] = destination_cave_piece
        unit.loc = destination

    def do_combat(self):
        num_rounds = 0
        try:
            while True:
                self.round()
                num_rounds += 1
        except NoTargetsFoundException:
            pass
        return num_rounds * self.remaining_hit_points()

    def remaining_hit_points(self):
        units = (cp for cp in self._rep.values() if isinstance(cp, Unit))
        return sum(unit.hit_points for unit in units)

    def round(self):
        turn_order = []
        for y in range(self.height):
            for x in range(self.width):
                loc = Location(x, y)
                cp = self.at(loc)
                if isinstance(cp, Unit):
                    turn_order.append(cp)
        for unit in turn_order:
            if unit.is_alive():
                unit.turn()

    def at(self, loc: Location):
        return self._rep.get(loc)

    def remove_unit_at(self, loc: Location):
        self._rep[loc] = Open(self, loc)

    def elf_count(self):
        return sum(1 for cp in self._rep.values() if isinstance(cp, Elf))


def part_1(txt):
    return Cave(txt).do_combat()


def part_2(txt):
    for elf_attack_power in itertools.count(start=4):
        c = Cave(txt, elf_attack_power=elf_attack_power)
        initial_elves = c.elf_count()
        result = c.do_combat()
        final_elves = c.elf_count()
        if initial_elves == final_elves:
            return result


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
