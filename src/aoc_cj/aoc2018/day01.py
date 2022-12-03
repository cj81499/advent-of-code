def parta(txt):
    return sum(int(x) for x in txt.splitlines())


def partb(txt):
    nums = [int(x) for x in txt.splitlines()]
    seen_freqs = set()
    i = 0
    while True:
        for n in nums:
            seen_freqs.add(i)
            i += n
            if i in seen_freqs:
                return i


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
