def parta(txt: str) -> int:
    total = 0
    for line in txt.splitlines():
        a, b = line.split(",")
        left = list(map(int, a.split("-")))
        right = list(map(int, b.split("-")))

        if (left[0] <= right[0] and left[1] >= right[1]) or (left[0] >= right[0] and left[1] <= right[1]):
            total += 1
    return total


def partb(txt: str) -> int:
    total = 0
    for line in txt.splitlines():
        a, b = line.split(",")
        left = list(map(int, a.split("-")))
        right = list(map(int, b.split("-")))

        if (
            right[0] <= left[0] <= right[1]
            or right[0] <= left[1] <= right[1]
            or left[0] <= right[0] <= left[1]
            or left[0] <= right[1] <= left[1]
        ):
            total += 1
    return total


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
