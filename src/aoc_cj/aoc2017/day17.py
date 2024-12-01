from collections import deque

TWO_THOUSAND_SEVENTEEN = 2017


def part_1(txt: str, element_after=TWO_THOUSAND_SEVENTEEN, loops=TWO_THOUSAND_SEVENTEEN):
    n = int(txt)
    d = deque([0])
    for i in range(loops):
        d.rotate(-n - 1)
        d.appendleft(i + 1)
    return d[(d.index(element_after) + 1) % len(d)]


def part_2(txt: str):
    return part_1(txt, element_after=0, loops=50000000)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
