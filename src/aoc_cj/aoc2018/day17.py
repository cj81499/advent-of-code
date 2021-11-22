import sys
from collections import Counter, defaultdict

sys.setrecursionlimit(2000)


class Scan:
    def __init__(self, lines: list):
        self.scan = defaultdict(lambda: ".")
        self.scan[(500, 0)] = "+"
        self.dimensions = {"min_x": None, "max_x": None, "min_y": None, "max_y": None}
        for line in lines:
            first_coord, second_coord = line.split(", ")
            first_coord_num = int(first_coord[2:])
            second_coord_nums = list(map(int, second_coord[2:].split("..")))
            area = {
                first_coord[0]: range(first_coord_num, first_coord_num + 1),
                second_coord[0]: range(second_coord_nums[0], second_coord_nums[1] + 1),
            }
            for x in area["x"]:
                for y in area["y"]:
                    self.scan[(x, y)] = "#"
            self.__expand_dimensions(area)

    def __str__(self) -> str:
        s = ""
        for y in range(self.dimensions["max_y"] + 2):
            for x in range(self.dimensions["min_x"] - 1, self.dimensions["max_x"] + 2):
                s += self.scan[(x, y)]
            if y != self.dimensions["max_y"] + 1:
                s += "\n"
        return s

    def __expand_dimensions(self, area: dict):
        area_dimensions = {
            "min_x": area["x"][0],
            "max_x": area["x"][len(area["x"]) - 1],
            "min_y": area["y"][0],
            "max_y": area["y"][len(area["y"]) - 1],
        }
        for d in self.dimensions:
            if self.dimensions[d] is not None:
                if d[:3] == "min":
                    self.dimensions[d] = min((self.dimensions[d], area_dimensions[d]))
                else:
                    self.dimensions[d] = max((self.dimensions[d], area_dimensions[d]))
            else:
                self.dimensions[d] = area_dimensions[d]

    def spread(self, x, y):
        if not self.scan[(x, y + 1)] in "~#":
            return
        left_done = False
        right_done = False
        left_hit_wall = 0
        left_reached_clif = 0
        right_hit_wall = 0
        right_reached_clif = 0
        i = 1
        while not left_done or not right_done:
            if not left_done:
                left_hit_wall = x - i + 1 if self.scan[x - i, y] == "#" else 0
                left_reached_clif = x - i + 1 if self.scan[x - i, y + 1] not in "~#" else 0
                left_done = left_hit_wall or left_reached_clif
            if not right_done:
                right_hit_wall = x + i - 1 if self.scan[x + i, y] == "#" else 0
                right_reached_clif = x + i - 1 if self.scan[x + i, y + 1] not in "~#" else 0
                right_done = right_hit_wall or right_reached_clif

            if not left_done:
                self.scan[(x - i, y)] = "|"
            if not right_done:
                self.scan[(x + i, y)] = "|"
            i += 1
        if right_hit_wall and left_hit_wall:
            for local_x in range(left_hit_wall, right_hit_wall + 1):
                self.scan[(local_x, y)] = "~"
        if right_reached_clif:
            self.drip(right_reached_clif + 1, y)
        if left_reached_clif:
            self.drip(left_reached_clif - 1, y)

    def drip(self, x, y):
        if not self.scan[(x, y)] == ".":
            return
        self.scan[(x, y)] = "|"
        # Stop when we reach bottom of map
        if y < self.dimensions["max_y"]:
            self.drip(x, y + 1)
            self.spread(x, y)

    def pour(self):
        self.drip(500, 1)

    def count_settled_water_tiles(self):
        c = Counter(self.scan.values())
        return c["~"]

    def count_all_water_tiles(self):
        c = Counter(self.scan.values())
        return c["~"] + c["|"]


def parta(txt):
    s = Scan(txt.splitlines())
    s.pour()
    return s.count_all_water_tiles() - (s.dimensions["min_y"] - 1)


def partb(txt):
    s = Scan(txt.splitlines())
    s.pour()
    return s.count_settled_water_tiles()


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
