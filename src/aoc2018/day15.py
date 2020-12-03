from collections import deque


class Cave:
    class Unit:
        ADJ_MOVES = [(0, 1), (-1, 0), (1, 0), (0, -1)]

        def __init__(self, unit_type, pos):
            self.type = unit_type
            self.pos = pos

        def __str__(self):
            return self.type

        def __repr__(self):
            return f"Unit({self.type}, {self.pos})"

        def is_same_race(self, other):
            if not isinstance(other, Cave.Unit):
                raise Exception
            return self.type == other.type

    def __init__(self, input_str):
        self.grid = [[(c if c not in "GE" else Cave.Unit(c, (x, y))) for x, c in enumerate(line)]
                     for y, line in enumerate(input_str)]

    def __str__(self):
        return "\n".join("".join(str(x) for x in row) for row in self.grid)

    def _move_order(self):
        order = deque()

        for y, row in enumerate(self.grid):
            for x, element in enumerate(row):
                if isinstance(element, Cave.Unit):
                    order.append(element)

        return order

    # def _valid_position(self, pos):
    #     x, y = pos
    #     if x < 0 or y < 0:
    #         return False
    #     if x >= len(self.grid[0]) or y >= len(self.grid):
    #         return False
    #     return True

    def _adj_units(self, pos):
        x, y = pos
        adj_grid_entries = [self.grid[y + b][x + a]
                            for (a, b) in Cave.Unit.ADJ_MOVES]
        adj_units = [x for x in adj_grid_entries if isinstance(x, Cave.Unit)]
        return adj_units

    def _adj_enemies(self, pos):
        x, y = pos
        unit: Cave.Unit = self.grid[y][x]
        if not isinstance(unit, Cave.Unit):
            raise Exception(f"Entry at {pos} is not a unit")
        adj_enemies = self._adj_units(pos)
        return adj_enemies

    def _unit_turn(self, unit):
        pos = unit.pos
        if not isinstance(unit, Cave.Unit):
            raise Exception(f"Entry at {pos} is not a unit")
        adj_enemies = self._adj_enemies(pos)

        print(pos, repr(unit), adj_enemies)

        # TODO: Finish unit_turn
        if len(adj_enemies) > 0:
            pass  # attack enemy
        else:
            pass  # move

    def _combat_round(self):
        move_order = self._move_order()

        while len(move_order) > 0:
            self._unit_turn(move_order.popleft())

    def combat(self):
        elves_alive = any(
            (isinstance(element, Cave.Unit) and element.type == "E" for element in row) for row in self.grid)
        goblins_alive = any(
            (isinstance(element, Cave.Unit) and element.type == "G" for element in row) for row in self.grid)
        print(elves_alive, goblins_alive)
        i = 0
        while elves_alive and goblins_alive and i < 20:
            self._combat_round()
            print(self)
            i += 1


def parta(cave: Cave):
    cave.combat()


def partb():
    pass


def main():
    _, input_lines = load_input(15, "Subterranean Sustainability")

    input_lines = """
#########
#GE.G..G#
#E......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########
""".strip().split("\n")

    cave = Cave(input_lines)
    print(f"parta: {parta(cave)}")
    # print(f"partb: {partb()}")


if __name__ == "__main__":
    from helpers import load_input
    main()
