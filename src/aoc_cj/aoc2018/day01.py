def part_1(txt):
    return sum(int(x) for x in txt.splitlines())


def part_2(txt):
    nums = [int(x) for x in txt.splitlines()]
    seen_freqs = set()
    i = 0
    while True:
        for n in nums:
            seen_freqs.add(i)
            i += n
            if i in seen_freqs:
                return i


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
