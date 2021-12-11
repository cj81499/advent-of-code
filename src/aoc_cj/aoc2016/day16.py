from more_itertools import ichunked


def step(data):
    a = data
    b = "".join("1" if c == "0" else "0" for c in reversed(a))
    return f"{a}0{b}"


def checksum(data):
    cs = "".join("1" if len(set(pair)) == 1 else "0" for pair in ichunked(data, 2))
    return checksum(cs) if len(cs) % 2 == 0 else cs


def parta(txt: str, length=272):
    data = txt
    while len(data) < length:
        data = step(data)
    return checksum(data[:length])


def partb(txt: str):
    return parta(txt, length=35651584)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
