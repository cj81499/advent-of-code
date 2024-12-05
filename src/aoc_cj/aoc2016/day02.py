NUMPAD_1 = """
123
456
789
"""


NUMPAD_2 = """
  1
 234
56789
 ABC
  D
"""


DIRECTION_TO_MOVE = {"U": -1j, "R": 1, "D": 1j, "L": -1}


def part_1(txt: str) -> str:
    return helper(txt, NUMPAD_1)


def part_2(txt: str) -> str:
    return helper(txt, NUMPAD_2)


def helper(code: str, numpad: str) -> str:
    pos_to_char = get_pos_to_char(numpad)
    result: list[str] = []
    pos = next(p for p, c in pos_to_char.items() if c == "5")
    for line in code.splitlines():
        for direction in line:
            new_pos = pos + DIRECTION_TO_MOVE[direction]
            if new_pos in pos_to_char:
                pos = new_pos
        result.append(pos_to_char[pos])
    return "".join(result)


def get_pos_to_char(numpad: str) -> dict[complex, str]:
    return {
        complex(x, y): c
        for y, line in enumerate(numpad.strip("\n").splitlines())
        for x, c in enumerate(line)
        if c != " "
    }


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
