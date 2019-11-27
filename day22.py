class Cave:
    regions = {}
    depth = 0

    class Region:
        def __init__(self, x, y, target_pos):
            self.x = x
            self.y = y
            if x == 0 and y == 0:
                self.geo_index = 0
            elif x == target_pos[0] and y == target_pos[1]:
                self.geo_index = 0
            elif y == 0:
                self.geo_index = x * 16807
            elif x == 0:
                self.geo_index = y * 48271
            else:
                self.geo_index = Cave.regions[(x - 1, y)].erosion_level * Cave.regions[(x, y - 1)].erosion_level
            self.erosion_level = (self.geo_index + Cave.depth) % 20183
            self.type_num = self.erosion_level % 3

        # def type
        @staticmethod
        def type_str(type_num):
            if type_num == 0:
                return "rocky"
            elif type_num == 1:
                return "wet"
            elif type_num == 2:
                return "narrow"
            else:
                raise Exception  # FIXME What kind of exception

        def __repr__(self):
            return f"x: {self.x}, y: {self.y}, geo: {self.geo_index}, ero: {self.erosion_level}, type: {self.type_str(self.type_num)}"  # noqa

        def __str__(self):
            if self.type_num == 0:
                return "."
            elif self.type_num == 1:
                return "="
            elif self.type_num == 2:
                return "|"
            else:
                raise Exception  # FIXME What kind of exception

    def __init__(self, depth, target_pos):
        Cave.depth = depth
        self.target_pos = target_pos

        Cave.regions[(0, 0)] = Cave.Region(0, 0, target_pos)
        for y in range(self.target_pos[1] + 1):
            for x in range(self.target_pos[0] + 1):
                Cave.regions[(x, y)] = Cave.Region(x, y, target_pos)
            # Cave.regions[(0, y)] = Cave.Region(0, y, target_pos)

        # for region in Cave.regions:
        # print(repr(Cave.regions[(0, 0)]))
        # print(repr(Cave.regions[(1, 0)]))
        # print(repr(Cave.regions[(0, 1)]))
        # print(repr(Cave.regions[(1, 1)]))
        # print(repr(Cave.regions[(10, 10)]))

        # print(self)

    def __str__(self):
        cave = []
        for y in range(self.target_pos[1] + 1):
            row = []
            for x in range(self.target_pos[0] + 1):
                if x == 0 and y == 0:
                    row.append("M")
                else:
                    row.append(str(self.regions[(x, y)]))
            cave.append("".join(row))
        return "\n".join(cave)

    def risk_level(self):
        risk = 0
        for y in range(self.target_pos[1] + 1):
            for x in range(self.target_pos[0] + 1):
                risk += self.regions[(x, y)].type_num
        return risk


def main():
    input_txt, input_lines = helpers.load_input(22, "Mode Maze")

    depth = int(input_lines[0][7:])
    target_x, target_y = map(int, input_lines[1][8:].split(","))

    c = Cave(depth, (target_x, target_y))
    print("part1:", c.risk_level())


if __name__ == "__main__":
    import helpers
    main()
