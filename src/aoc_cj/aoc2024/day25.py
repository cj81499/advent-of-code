import itertools

import more_itertools as mi


def height(key_or_lock: list[str]) -> tuple[int, ...]:
    columns: zip[tuple[str, ...]] = zip(*key_or_lock[1:-1], strict=True)
    return tuple(col.count("#") for col in columns)


def fit_together(key: list[int], lock: list[int]) -> bool:
    return all(a + b < 6 for a, b in zip(lock, key, strict=True))


def part_1(txt: str) -> int:
    keys_or_locks = (kol.splitlines() for kol in txt.split("\n\n"))
    buckets = mi.bucket(keys_or_locks, key=lambda kol: kol[0])
    lock_heights = map(height, buckets["#####"])
    key_heights = map(height, buckets["....."])
    return sum(itertools.starmap(fit_together, itertools.product(lock_heights, key_heights)))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
