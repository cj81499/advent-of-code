def part_1(txt):
    nums = {int(line) for line in txt.splitlines()}

    for n in nums:
        remaining = 2020 - n
        if remaining in nums:
            return n * remaining


def part_2(txt):
    nums = {int(line) for line in txt.splitlines()}

    for x in nums:
        for y in nums:
            remaining = 2020 - (x + y)
            if remaining in nums:
                return x * y * remaining


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
