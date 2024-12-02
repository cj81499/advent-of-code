def decode(s: str) -> str:
    str_in_mem: list[str] = []

    # start at 1 and end at len(s) -1 to ignore quotation marks
    i = 1
    while i < len(s) - 1:
        pair = s[i : i + 2]
        if pair == "\\\\":
            str_in_mem.append("\\")
            i += 1
        elif pair == '\\"':
            str_in_mem.append('"')
            i += 1
        elif pair == "\\x":
            str_in_mem.append(chr(int(s[i + 2 : i + 4], base=16)))
            i += 3
        else:
            str_in_mem.append(s[i])
        i += 1

    return "".join(str_in_mem)


def encode(s: str) -> str:
    str_in_mem: list[str] = []

    str_in_mem.append('"')
    for c in s:
        if c == "\\":
            str_in_mem.append("\\\\")
        elif c == '"':
            str_in_mem.append('\\"')
        else:
            str_in_mem.append(c)
    str_in_mem.append('"')

    return "".join(str_in_mem)


def part_1(txt: str) -> int:
    total_chars_of_code = 0
    total_chars_in_memory = 0
    for s in txt.splitlines():
        total_chars_of_code += len(s)
        total_chars_in_memory += len(decode(s))

    return total_chars_of_code - total_chars_in_memory


def part_2(txt: str) -> int:
    total_chars_of_original = 0
    total_chars_of_encoded = 0
    for s in txt.splitlines():
        total_chars_of_original += len(s)
        total_chars_of_encoded += len(encode(s))

    return total_chars_of_encoded - total_chars_of_original


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
