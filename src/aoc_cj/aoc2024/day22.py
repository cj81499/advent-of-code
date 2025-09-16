import itertools
from collections import defaultdict
from collections.abc import Generator, Iterable

import more_itertools as mi


def nth[T](iterable: Iterable[T], n: int) -> T:
    return mi.first(itertools.islice(iterable, n, None))


def secret_generator(secret: int) -> Generator[int]:
    while True:
        secret ^= secret * 64
        secret %= 16777216
        secret ^= secret // 32
        secret %= 16777216
        secret ^= secret * 2048
        secret %= 16777216
        yield secret


def part_1(txt: str) -> int:
    return sum(nth(secret_generator(initial_secret), 2000 - 1) for initial_secret in map(int, txt.splitlines()))


PriceChanges = tuple[int, ...]
Secret = int
Price = int


def part_2(txt: str) -> int:
    price_for_changes = defaultdict[PriceChanges, dict[Secret, Price]](dict)
    for initial_secret in map(int, txt.splitlines()):
        gen = secret_generator(initial_secret)
        first_2000_secrets = itertools.islice(gen, 2000)
        for secrets in mi.sliding_window(first_2000_secrets, 5):
            prices = tuple(s % 10 for s in secrets)
            sale_price = prices[-1]
            price_changes = tuple(b - a for a, b in itertools.pairwise(prices))
            price_for_changes[price_changes].setdefault(initial_secret, sale_price)
    return max(sum(prices.values()) for prices in price_for_changes.values())


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
