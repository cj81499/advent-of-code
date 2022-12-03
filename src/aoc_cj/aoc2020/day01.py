def parta(txt):
    nums = {int(line) for line in txt.splitlines()}

    for n in nums:
        remaining = 2020 - n
        if remaining in nums:
            return n * remaining


def partb(txt):
    nums = {int(line) for line in txt.splitlines()}

    for x in nums:
        for y in nums:
            remaining = 2020 - (x + y)
            if remaining in nums:
                return x * y * remaining


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
