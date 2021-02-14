from __future__ import annotations

import re
from collections import Counter

ROOM_REGEX = re.compile(r"([\w-]+)-(\d+)\[(\w+)\]")


def parta(txt: str):
    return sum(
        sector_id(line) for line in txt.splitlines()
        if is_real_room(line)
    )


def partb(txt: str):
    for line in txt.splitlines():
        if is_real_room(line):
            decrypted = decrypt(line)
            if "north" in decrypted and "pole" in decrypted:
                return sector_id(line)


def sector_id(room: str):
    _name, sector_id, _provided_checksum = ROOM_REGEX.match(room).groups()
    return int(sector_id)


def is_real_room(room: str):
    name, _sector_id, provided_checksum = ROOM_REGEX.match(room).groups()
    name = name.replace("-", "")
    counts = Counter(name).items()
    alphabetized_counts = sorted(counts, key=lambda x: x[0])
    sorted_counts = sorted(alphabetized_counts, key=lambda x: x[1], reverse=True)
    checksum = "".join(letter for letter, _count in sorted_counts)
    return checksum.startswith(provided_checksum)


def decrypt(room: str):
    name, sector_id, _provided_checksum = ROOM_REGEX.match(room).groups()
    new_name = []
    for c in name:
        if c == "-":
            c = " "
        else:
            for _ in range(int(sector_id)):
                c = "a" if c == "z" else chr(ord(c) + 1)
        new_name.append(c)
    return "".join(new_name)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
