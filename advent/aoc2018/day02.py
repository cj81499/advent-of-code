from collections import Counter


def parta(txt):
    lines = txt.splitlines()
    c2 = 0
    c3 = 0
    for line in lines:
        s = set(Counter(line).values())
        if 2 in s:
            c2 += 1
        if 3 in s:
            c3 += 1
    return c2 * c3


def partb(txt):
    lines = txt.splitlines()
    for i, s1 in enumerate(lines):
        for s2 in lines[i:]:
            if sum([1 for k in range(len(s1)) if s1[k] != s2[k]]) == 1:
                return "".join([s1[k] for k in range(len(s1)) if s1[k] == s2[k]])


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
