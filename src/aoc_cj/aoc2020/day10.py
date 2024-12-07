from functools import cache


def get_adapters(txt):
    adapters = [int(line) for line in txt.splitlines()]
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return adapters


def part_1(txt):
    adapters = get_adapters(txt)

    joltage = 0
    diffs = [0, 0, 0, 0]
    for adapter in adapters:
        diff = adapter - joltage
        diffs[diff] += 1
        joltage = adapter

    return diffs[1] * diffs[3]


def valid_next_adapters(joltage, adapters):
    return {joltage + i for i in range(1, 4)}.intersection(adapters)


@cache
def part_2_helper(joltage, adapters):
    if joltage == max(adapters):
        return 1
    return sum(part_2_helper(adapter, adapters) for adapter in valid_next_adapters(joltage, adapters))


def part_2(txt):
    return part_2_helper(0, frozenset(get_adapters(txt)))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
