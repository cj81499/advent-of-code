def parta(lines: list):
    d = 1000
    x = [0 for i in range(d)]
    grid = [x.copy() for i in range(d)]
    for line in lines:
        s = line.split(" ")
        left, top = [int(x) for x in s[2][:-1].split(",")]
        width, height = [int(x) for x in s[3].split("x")]
        for y in range(height):
            for x in range(width):
                grid[top + y][left + x] += 1
    count = 0
    for y in grid:
        for x in y:
            if x >= 2:
                count += 1
    return count


def partb(lines: list): # noqa
    d = 1000
    x = ["0" for i in range(d)]
    grid = [x.copy() for i in range(d)]
    for line in lines:
        s = line.split(" ")
        claim_num = int(s[0][1:])
        left, top = [int(x) for x in s[2][:-1].split(",")]
        width, height = [int(x) for x in s[3].split("x")]
        for y in range(height):
            for x in range(width):
                if grid[top + y][left + x] == "0":
                    grid[top + y][left + x] = claim_num
                else:
                    grid[top + y][left + x] = "X"
    for line in lines:
        s = line.split(" ")
        claim_num = int(s[0][1:])
        left, top = [int(x) for x in s[2][:-1].split(",")]
        width, height = [int(x) for x in s[3].split("x")]
        claim_valid = True
        for y in range(height):
            for x in range(width):
                if grid[top + y][left + x] != claim_num:
                    claim_valid = False
                if not claim_valid:
                    break
        if claim_valid:
            return claim_num


def main():
    _, input_lines = helpers.load_input(3, "No Matter How You Slice It")

    print(f"parta: {parta(input_lines)}")
    print(f"partb: {partb(input_lines)}")


if __name__ == "__main__":
    import helpers
    main()
