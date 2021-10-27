CONFUSING = {"i", "o", "l"}


def next_valid_password(txt: str) -> str:
    password = fast_increment_password(txt)
    while not is_valid_password(password):
        password = fast_increment_password(password)
    return password


def next_char(c: str) -> str:
    assert len(c) == 1
    return chr(ord(c) + 1)


def fast_increment_password(txt: str) -> str:
    for i, c in enumerate(txt):
        if c in CONFUSING:
            return "".join(txt[:i]) + next_char(c) + ("a" * (len(txt) - (i + 1)))

    return increment_password(txt)


def increment_password(txt: str) -> str:
    if len(txt) == 0:
        return "a"
    if txt[-1] == "z":
        return increment_password(txt[:-1]) + "a"
    return txt[:-1] + next_char(txt[-1])


def is_valid_password(txt: str) -> bool:
    # Passwords must include one increasing straight of at least three letters,
    # like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    # Passwords may not contain the letters i, o, or l, as these letters can
    # be mistaken for other characters and are therefore confusing.
    # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    straight = False
    pairs = set()

    for i in range(len(txt)):
        if txt[i] in CONFUSING:
            return False
        if i < len(txt) - 1:
            c1, c2 = txt[i], txt[i + 1]
            if c1 == c2:
                pairs.add(c1)
        if not straight and i < len(txt) - 2:
            c3 = txt[i + 2]
            if ord(c1) == ord(c2) - 1 and ord(c1) == ord(c3) - 2:
                straight = True

    return straight and len(pairs) >= 2


def parta(txt):
    return next_valid_password(txt)


def partb(txt):
    return next_valid_password(next_valid_password(txt))


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
