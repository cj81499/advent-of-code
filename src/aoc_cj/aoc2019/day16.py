from itertools import chain, cycle, repeat


def digits(s: str):
    return [int(c) for c in s]


BASE_PATTERN = [0, 1, 0, -1]


def pattern_helper(i):
    p = cycle(chain.from_iterable(repeat(n, i + 1) for n in BASE_PATTERN))
    next(p)  # skip first
    return p


def phase(digits):
    next_list = []
    for i in range(len(digits)):
        pattern = pattern_helper(i)
        val = abs(sum(p * d for p, d in zip(pattern, digits))) % 10
        next_list.append(val)
    return next_list


def part_1(txt: str):
    d = digits(txt)
    for _ in range(100):
        d = phase(d)
    return "".join(map(str, d[:8]))


def part_2(txt: str):
    offset = int(txt[:7])
    # since the offset is over halfway through the list all the digits will be muiltiplied by 1
    # therefore, the new digit is simply the last digit of the sum of all digits at and after that position
    assert offset > ((len(txt) * 10000) / 2)
    d = digits(txt * 10000)[offset:]
    for _ in range(100):
        new_d = []
        s = sum(d)
        for x in d:
            new_d.append(s % 10)
            s -= x
        d = new_d
    return "".join(map(str, d[:8]))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
