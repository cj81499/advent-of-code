def parta(txt):
    nums = set(int(line) for line in txt.splitlines())

    for n in nums:
        remaining = 2020 - n
        if remaining in nums:
            return n * remaining


def partb(txt):
    nums = set(int(line) for line in txt.splitlines())

    for x in nums:
        for y in nums:
            remaining = 2020 - (x + y)
            if remaining in nums:
                return x * y * remaining


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
