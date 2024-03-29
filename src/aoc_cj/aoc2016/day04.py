import re
from collections import Counter

ROOM_REGEX = re.compile(r"([\w-]+)-(\d+)\[(\w+)\]")


def part_1(txt: str):
    return sum(sector_id(line) for line in txt.splitlines() if is_real_room(line))


def part_2(txt: str):
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


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
