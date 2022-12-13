def parta(txt):
    return sum(int(c) for i, c in enumerate(txt) if c == txt[i - 1])


def partb(txt):
    return sum(int(c) for i, c in enumerate(txt) if c == txt[i - len(txt) // 2])


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
