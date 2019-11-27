from collections import Counter


def part1(s: str):
    c = Counter(s)
    return c["("] - c[")"]


def part2(s: str):
    floor = 0
    for i, x in enumerate(s):
        floor += 1 if x == "(" else - 1
        if floor == -1:
            return i + 1


def main():
    input_txt, _ = helpers.load_input(1, "Not Quite Lisp")

    print(f"part1: {part1(input_txt)}")
    print(f"part2: {part2(input_txt)}")


if __name__ == "__main__":
    import helpers
    main()
