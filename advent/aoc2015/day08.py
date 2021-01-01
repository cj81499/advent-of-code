from datetime import date

import helpers


def decode(s: str) -> int:
    str_in_mem = []

    # start at 1 and end at len(s) -1 to ignore quotation marks
    i = 1
    while i < len(s) - 1:
        pair = s[i:i + 2]
        if pair == "\\\\":
            str_in_mem.append("\\")
            i += 1
        elif pair == "\\\"":
            str_in_mem.append("\"")
            i += 1
        elif pair == "\\x":
            str_in_mem.append(chr(int(s[i + 2:i + 4], base=16)))
            i += 3
        else:
            str_in_mem.append(s[i])
        i += 1

    return "".join(str_in_mem)


def encode(s: str) -> int:
    str_in_mem = []

    str_in_mem.append("\"")
    for c in s:
        if c == "\\":
            str_in_mem.append("\\\\")
        elif c == "\"":
            str_in_mem.append("\\\"")
        else:
            str_in_mem.append(c)
    str_in_mem.append("\"")

    return "".join(str_in_mem)


def part1(lines: list):
    total_chars_of_code = 0
    total_chars_in_memory = 0
    for s in lines:
        total_chars_of_code += len(s)
        total_chars_in_memory += len(decode(s))

    return total_chars_of_code - total_chars_in_memory


def part2(lines: list):
    total_chars_of_original = 0
    total_chars_of_encoded = 0
    for s in lines:
        total_chars_of_original += len(s)
        total_chars_of_encoded += len(encode(s))

    return total_chars_of_encoded - total_chars_of_original


def main():
    _, input_lines = helpers.get_puzzle(date(2015, 12, 8), "Matchsticks")  # noqa

    print(f"part1: {part1(input_lines)}")
    print(f"part2: {part2(input_lines)}")


if __name__ == "__main__":
    main()
