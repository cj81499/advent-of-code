from itertools import combinations

LITERS = 150


def get_good_combos(txt: str, *, liters: int = LITERS) -> list[tuple[int, ...]]:
    containers = list(map(int, txt.splitlines()))
    good: list[tuple[int, ...]] = []
    for i in range(len(containers)):
        size_good = [x for x in combinations(containers, i) if sum(x) == liters]
        good.extend(size_good)
    return good


def part_1(txt: str, *, liters: int = LITERS) -> int:
    return len(get_good_combos(txt, liters=liters))


def part_2(txt: str, *, liters: int = LITERS) -> int:
    good_combos = get_good_combos(txt, liters=liters)
    min_len = min(map(len, good_combos))
    return sum(1 for x in good_combos if len(x) == min_len)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
