from aoc_cj.util import adj_8


def parse(txt: str) -> set[complex]:
    return {complex(x, y) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c == "@"}


def accessible(paper: set[complex]) -> set[complex]:
    return {p for p in paper if sum(p in paper for p in adj_8(p)) < 4}


def part_1(txt: str) -> int:
    return len(accessible(parse(txt)))


def part_2(txt: str) -> int:
    original_paper = parse(txt)
    paper = original_paper.copy()
    while a := accessible(paper):
        paper -= a
    return len(original_paper - paper)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
