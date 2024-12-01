import collections


def part_1(txt: str) -> int:
    lefts = []
    rights = []
    for line in txt.splitlines():
        l, r = line.split()
        lefts.append(int(l))
        rights.append(int(r))
    lefts = sorted(lefts)
    rights = sorted(rights)
    s = 0
    for l, r in zip(sorted(lefts), sorted(rights)):
        diff = abs(l - r)
        s += diff
    return s


def part_2(txt: str) -> int:
    sim_score = 0
    lefts = []
    rights = []
    for line in txt.splitlines():
        l, r = line.split()
        lefts.append(int(l))
        rights.append(int(r))
    rights = collections.Counter(rights)
    for l in lefts:
        sim_score += l * rights[l]
    return sim_score


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
