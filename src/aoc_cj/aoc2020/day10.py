from functools import cache


def get_adapters(txt):
    adapters = [int(line) for line in txt.splitlines()]
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return adapters


def parta(txt):
    adapters = get_adapters(txt)

    joltage = 0
    diffs = [0, 0, 0, 0]
    for adapter in adapters:
        diff = adapter - joltage
        diffs[diff] += 1
        joltage = adapter

    return diffs[1] * diffs[3]


def valid_next_adapters(joltage, adapters):
    return set(joltage + i for i in range(1, 4)).intersection(adapters)


@cache
def partb_helper(joltage, adapters):
    if joltage == max(adapters):
        return 1
    return sum(partb_helper(adapter, adapters) for adapter in valid_next_adapters(joltage, adapters))


def partb(txt):
    return partb_helper(0, frozenset(get_adapters(txt)))


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
