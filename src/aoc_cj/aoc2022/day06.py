import more_itertools as mi


def parta(txt: str, n: int = 4) -> int:
    return mi.first(i for i, chars in enumerate(mi.windowed(txt, n), start=n) if mi.all_unique(chars))


def partb(txt: str) -> int:
    return parta(txt, 14)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
