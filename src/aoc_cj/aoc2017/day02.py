import itertools


def part_1(txt):
    spreadsheet = [[int(n) for n in line.split()] for line in txt.splitlines()]
    return sum(max(row) - min(row) for row in spreadsheet)


def part_2(txt):
    spreadsheet = [[int(n) for n in line.split()] for line in txt.splitlines()]
    return sum(m // n for row in spreadsheet for m, n in itertools.permutations(row, r=2) if m % n == 0)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
