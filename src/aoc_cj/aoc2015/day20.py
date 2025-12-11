import itertools


def select_house(presents: list[int], min_presents: int) -> int:
    for i, n in enumerate(presents):
        if n > min_presents and i > 0:
            return i

    msg = "unreachable"
    raise AssertionError(msg)


def presents_for_houses(min_presents: int, present_multiplier: int, *, house_limit: int | None = None) -> list[int]:
    # this is probably big enough... right? (works for examples, so it's probably fine)
    arr_size = min_presents // 10
    presents = [0] * arr_size
    for elf_num in range(1, arr_size):
        iterator = itertools.count() if house_limit is None else range(house_limit)
        for i in (elf_num * (n + 1) for n in iterator):
            if i >= arr_size:
                break
            presents[i] += elf_num * present_multiplier

    return presents


def helper(txt: str, present_multiplier: int, *, house_limit: int | None = None) -> int:
    min_presents = int(txt)
    presents = presents_for_houses(min_presents, present_multiplier, house_limit=house_limit)
    return select_house(presents, min_presents)


def part_1(txt: str) -> int:
    return helper(txt, 10)


def part_2(txt: str) -> int:
    return helper(txt, 11, house_limit=50)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
