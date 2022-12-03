from functools import reduce

from more_itertools import chunked, only


def get_common_item(*strings: str) -> str:
    intersection = reduce(lambda x, y: x & y, (set(s) for s in strings))
    common = only(intersection)
    assert common is not None
    return common


def priority(c: str) -> int:
    assert len(c) == 1
    return ord(c.lower()) - ord("a") + (1 if c.islower() else 27)


def parta(txt: str) -> int:
    return sum(priority(get_common_item(l[: len(l) // 2], l[len(l) // 2 :])) for l in txt.splitlines())


def partb(txt: str) -> int:
    return sum(priority(get_common_item(*chunk)) for chunk in chunked(txt.splitlines(), 3))


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
