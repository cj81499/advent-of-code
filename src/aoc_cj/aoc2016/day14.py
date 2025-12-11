import hashlib
import itertools
from collections.abc import Callable, Generator

import more_itertools as mi

REQUIRED_KEYS = 64


def n_repeat_character(s: str, n: int) -> str | None:
    """Return the first character in `s` that occurs `n` (or more) times in a row, or `None` if no such character exists."""
    return mi.first((c for c, length in mi.run_length.encode(s) if length >= n), default=None)


def standard_hash(to_hash: str) -> str:
    return hashlib.md5(to_hash.encode()).hexdigest()  # noqa: S324


def key_stretch_hash(to_hash: str) -> str:
    h = standard_hash(to_hash)
    for _ in range(2016):
        h = standard_hash(h)
    return h


def keys(salt: str, hash_fn: Callable[[str], str] = standard_hash) -> Generator[int]:
    idx_chr_pairs = set[tuple[int, str]]()  # (idx, char)
    validated = set[tuple[int, str]]()

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


def part_1(txt: str) -> int:
    res = mi.nth(keys(txt), REQUIRED_KEYS - 1)
    assert res is not None
    return res


def part_2(txt: str) -> int:
    res = mi.nth(keys(txt, hash_fn=key_stretch_hash), REQUIRED_KEYS - 1)
    assert res is not None
    return res


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
