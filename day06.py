from grid import Grid


# TODO Revist b/c this is slow

def part1(lines: list):
    g = Grid((1000, 1000), default_value=False)
    for instruction in lines:
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


def part2(lines: list):
    g = Grid((1000, 1000), default_value=0)
    for instruction in lines:
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


def main():
    _, input_lines = helpers.load_input(6, "Probably a Fire Hazard")

    print(f"part1: {part1(input_lines)}")
    print(f"part2: {part2(input_lines)}")


if __name__ == "__main__":
    import helpers
    main()
