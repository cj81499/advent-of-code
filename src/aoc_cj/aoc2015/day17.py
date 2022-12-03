from itertools import combinations

LITERS = 150


def get_good_combos(txt, liters=LITERS):
    containers = list(map(int, txt.splitlines()))
    good = []
    for i in range(len(containers)):
        size_good = [x for x in combinations(containers, i) if sum(x) == liters]
        good.extend(size_good)
    return good


def parta(txt, liters=LITERS):
    return len(get_good_combos(txt, liters=liters))


def partb(txt, liters=LITERS):
    good_combos = get_good_combos(txt, liters=liters)
    min_len = min(map(len, good_combos))
    return sum(1 for x in good_combos if len(x) == min_len)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
