import re

FIRST_CODE = 20151125


def next_code(code: int) -> int:
    return (code * 252533) % 33554393


def code_at(col: int, row: int) -> int:
    code = FIRST_CODE
    x, y = 1, 1

    while not (x == col and y == row):
        code = next_code(code)
        if y == 1:
            x, y = 1, x + 1
        else:
            x, y = x + 1, y - 1
    return code


PARSE_REGEX = re.compile(r".* row (\d+), column (\d+).")


def part_1(txt: str) -> int:
    match = PARSE_REGEX.match(txt)
    if not match:
        raise ValueError("bad input")
    row, col = map(int, match.groups())
    return code_at(col, row)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
