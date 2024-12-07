import itertools
from hashlib import md5

from more_itertools import windowed

REQUIRED_KEYS = 64


def n_repeat_character(h: str, n):
    for chars in windowed(h, n):  # for each view of size n
        if len(set(chars)) == 1:  # if the view only contains one character repeated n times
            return chars[0]  # return the character
    return None  # if no such repeat exists, return None


def standard_hash(to_hash: str):
    return md5(to_hash.encode()).hexdigest()


def key_stretch_hash(to_hash):
    h = standard_hash(to_hash)
    for _ in range(2016):
        h = standard_hash(h)
    return h


def keys(salt, hash_fn=standard_hash):
    idx_chr_pairs = set()  # (idx, char)
    validated = set()

    for i in itertools.count():
        h = hash_fn(f"{salt}{i}")

        if (c := n_repeat_character(h, 5)) is not None:
            # remove pairs that are too old to be valid
            old_pairs = {p for p in idx_chr_pairs if i - p[0] >= 1000}
            idx_chr_pairs -= old_pairs

            # update validated with the pairs that are made valid by the new hash
            validated.update(p for p in idx_chr_pairs if c == p[1])
            idx_chr_pairs -= validated

            # yield values only once that are guaranteed to NOT have other valid values before them
            ready_to_yield = {p for p in validated if i - p[0] >= 1000}
            yield from sorted(p[0] for p in ready_to_yield)  # yield in increasing order
            validated -= ready_to_yield

        if (c := n_repeat_character(h, 3)) is not None:
            idx_chr_pairs.add((i, c))


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(itertools.islice(iterable, n, None), default)


def part_1(txt: str):
    return nth(keys(txt), REQUIRED_KEYS - 1)


def part_2(txt: str):
    return nth(keys(txt, hash_fn=key_stretch_hash), REQUIRED_KEYS - 1)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
