from collections import deque

TWO_THOUSAND_SEVENTEEN = 2017


def parta(txt: str, element_after=TWO_THOUSAND_SEVENTEEN, loops=TWO_THOUSAND_SEVENTEEN):
    n = int(txt)
    d = deque([0])
    for i in range(loops):
        d.rotate(-n - 1)
        d.appendleft(i + 1)
    return d[(d.index(element_after) + 1) % len(d)]


def partb(txt: str):
    return parta(txt, element_after=0, loops=50000000)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
