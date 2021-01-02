class Grid():
    def __init__(self, dimensions, default_value=None):
        self.grid = {}
        self._default_value = default_value
        for y in range(dimensions[1]):
            for x in range(dimensions[0]):
                self.grid[(x, y)] = self._default_value

    def __getitem__(self, key):
        return self.grid[key]

    def __setitem__(self, key, value):
        self.grid[key] = value

    def __delitem__(self, key):
        self.grid[key] = self._default_value


# TODO Revist b/c this is slow

def parta(txt):
    g = Grid((1000, 1000), default_value=False)
    for instruction in txt.splitlines():
        words = instruction.split()
        if words[0] == "toggle":
            start = [int(x) for x in words[1].split(",")]
            stop = [int(x) for x in words[3].split(",")]
            for y in range(start[1], stop[1] + 1):
                for x in range(start[0], stop[0] + 1):
                    g[(x, y)] = not g[(x, y)]
        else:
            start = [int(x) for x in words[2].split(",")]
            stop = [int(x) for x in words[4].split(",")]
            value = words[1] == "on"
            for y in range(start[1], stop[1] + 1):
                for x in range(start[0], stop[0] + 1):
                    g[(x, y)] = value
    count = sum(g[(x, y)] for x in range(1000) for y in range(1000))
    return count


def partb(txt):
    g = Grid((1000, 1000), default_value=0)
    for instruction in txt.splitlines():
        words = instruction.split()
        if words[0] == "toggle":
            start = [int(x) for x in words[1].split(",")]
            stop = [int(x) for x in words[3].split(",")]
            for y in range(start[1], stop[1] + 1):
                for x in range(start[0], stop[0] + 1):
                    g[(x, y)] += 2
        else:
            start = [int(x) for x in words[2].split(",")]
            stop = [int(x) for x in words[4].split(",")]
            value = 1 if words[1] == "on" else -1
            for y in range(start[1], stop[1] + 1):
                for x in range(start[0], stop[0] + 1):
                    g[(x, y)] = max(g[(x, y)] + value, 0)
    count = sum(g[(x, y)] for x in range(1000) for y in range(1000))
    return count


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
