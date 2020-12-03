from collections import Counter


def parta(input_lines: list):
    c2 = 0
    c3 = 0
    for l in input_lines:
        s = set(Counter(l).values())
        if 2 in s:
            c2 += 1
        if 3 in s:
            c3 += 1
    return c2 * c3


def partb(input_lines: list):
    for i, s1 in enumerate(input_lines):
        for s2 in input_lines[i:]:
            if sum([1 for k in range(len(s1)) if s1[k] != s2[k]]) == 1:
                return "".join([s1[k] for k in range(len(s1)) if s1[k] == s2[k]])


def main():
    _, input_lines = helpers.load_input(2, "Inventory Management System")

    print(f"parta: {parta(input_lines)}")
    print(f"partb: {partb(input_lines)}")


if __name__ == "__main__":
    import helpers
    main()
