from more_itertools import pairwise, triplewise


def nums(txt: str) -> list[int]:
    return list(map(int, txt.splitlines()))


def parta(txt: str) -> int:
    return sum(b > a for a, b in pairwise(nums(txt)))


def partb(txt: str) -> int:
    sums = (sum(w) for w in triplewise(nums(txt)))
    return sum(b > a for a, b in pairwise(sums))


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
