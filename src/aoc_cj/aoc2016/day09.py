from __future__ import annotations

import re

MARKER_REGEX = re.compile(r"^\((\d+)x(\d+)\)")


def parta(txt: str):
    return decompressed_length(txt)


def partb(txt: str):
    return decompressed_length(txt, recursive=True)


def decompressed_length(s: str, recursive=False):
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


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
