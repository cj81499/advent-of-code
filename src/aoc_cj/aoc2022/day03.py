from more_itertools import chunked, only


def parta(txt: str) -> int:
    total = 0
    for line in txt.splitlines():
        first_half = line[: len(line) // 2]
        second_half = line[len(line) // 2 :]
        common_item = only(set(first_half).intersection(set(second_half)))
        assert common_item is not None
        total += priority(common_item)
    return total


def priority(c: str) -> int:
    assert len(c) == 1
    return ord(c.lower()) - ord("a") + (1 if c.islower() else 27)


def partb(txt: str) -> int:
    total = 0
    for chunk in chunked(txt.splitlines(), 3):
        assert len(chunk) == 3
        a, b, c = chunk
        common_item = only(set(a).intersection(set(b)).intersection(set(c)))
        assert common_item is not None
        total += priority(common_item)

    return total


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
