import itertools
from collections.abc import Generator

import more_itertools

CONFUSING = {"i", "o", "l"}


def generate_passwords(after: str) -> Generator[str, None, None]:
    pw = after
    while True:
        pw = increment_password(pw)
        if is_valid_password(pw):
            yield pw


def next_char(c: str) -> str:
    assert len(c) == 1
    c = chr(ord(c) + 1)
    return c if c not in CONFUSING else next_char(c)


def increment_password(txt: str) -> str:
    if len(txt) == 0:
        return "a"
    if txt[-1] == "z":
        return increment_password(txt[:-1]) + "a"
    return txt[:-1] + next_char(txt[-1])


def is_valid_password(txt: str) -> bool:
    # Passwords may not contain the letters i, o, or l, as these letters can
    # be mistaken for other characters and are therefore confusing.
    if any(c in CONFUSING for c in txt):
        return False

    # Passwords must include one increasing straight of at least three letters,
    # like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    if not any(True for a, b, c in more_itertools.triplewise(txt) if ord(a) + 2 == ord(b) + 1 == ord(c)):
        return False

    # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    pair_count = len(set(a for a, b in itertools.pairwise(txt) if a == b))
    if pair_count < 2:
        return False

    return True


def part_1(txt: str) -> str:
    return more_itertools.first(generate_passwords(txt))


def part_2(txt: str) -> str:
    res = more_itertools.nth(generate_passwords(txt), 1)
    assert res is not None, "Unreachable. There are infinite valid passwords."
    return res


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
