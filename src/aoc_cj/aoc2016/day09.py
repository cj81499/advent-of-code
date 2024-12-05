import re

MARKER_REGEX = re.compile(r"^\((\d+)x(\d+)\)")


def part_1(txt: str) -> int:
    return decompressed_length(txt)


def part_2(txt: str) -> int:
    return decompressed_length(txt, recursive=True)


def decompressed_length(s: str, *, recursive: bool = False) -> int:
    length = 0
    i = 0
    while i < len(s):
        if s[i] != "(":
            length += 1
            i += 1
        elif match := MARKER_REGEX.match(s[i:]):
            l, repeat = map(int, match.groups())
            length += repeat * (
                l if not recursive else decompressed_length(s[i + match.end() : i + match.end() + l], recursive=True)
            )
            i += match.end() + l
    return length


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
