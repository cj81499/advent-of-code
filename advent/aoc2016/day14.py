from __future__ import annotations

import itertools
from hashlib import md5

REQUIRED_KEYS = 64


def groupwise(iterable, n):
    for i in range(len(iterable) - n + 1):
        yield iterable[i: i+n]


def n_repeat_character(h: str, n):
    for chars in groupwise(h, n):  # for each view of size n
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
            old_pairs = set(p for p in idx_chr_pairs if i - p[0] >= 1000)
            idx_chr_pairs -= old_pairs

            # update validated with the pairs that are made valid by the new hash
            validated.update(p for p in idx_chr_pairs if c == p[1])
            idx_chr_pairs -= validated

            # yield values only once that are guaranteed to NOT have other valid values before them
            ready_to_yield = set(p for p in validated if i - p[0] >= 1000)
            yield from sorted(p[0] for p in ready_to_yield)  # yield in increasing order
            validated -= ready_to_yield

        if (c := n_repeat_character(h, 3)) is not None:
            idx_chr_pairs.add((i, c))


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(itertools.islice(iterable, n, None), default)


def parta(txt: str):
    return nth(keys(txt), REQUIRED_KEYS - 1)


def partb(txt: str):
    return nth(keys(txt, hash_fn=key_stretch_hash), REQUIRED_KEYS - 1)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
