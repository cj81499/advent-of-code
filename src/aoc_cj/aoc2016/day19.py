import itertools

# Explanation: notice a pattern in the first few outputs (when they're still easy to compute)
# then, just keep the pattern going!


def part_1(txt: str):
    def pattern():
        for i in itertools.count():
            yield from range(1, 2**i, 2)

    return next(itertools.islice(pattern(), int(txt) - 1, None))


def part_2(txt: str):
    def pattern():
        for i in itertools.count():
            yield from (n for n in range(1, 3**i + 1) if n < 3 ** (i - 1) or n % 2 != 0)

    return next(itertools.islice(pattern(), int(txt) - 1, None))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
