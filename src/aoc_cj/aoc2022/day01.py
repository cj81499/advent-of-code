def parta(txt: str) -> None:
    chunks = txt.split("\n\n")

    chunk_sums = [sum(int(n) for n in chunk.splitlines()) for chunk in chunks]
    print(chunk_sums)
    return max(chunk_sums)


def partb(txt: str) -> None:
    chunks = txt.split("\n\n")

    chunk_sums = [sum(int(n) for n in chunk.splitlines()) for chunk in chunks]
    print(chunk_sums)
    a = max(chunk_sums)
    chunk_sums.remove(a)
    b = max(chunk_sums)
    chunk_sums.remove(b)
    c = max(chunk_sums)
    return a + b + c


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
