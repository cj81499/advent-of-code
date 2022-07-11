import itertools
from collections.abc import Iterable

FOURTY_MILLION = 40_000_000
FIVE_MILLION = 5_000_000

DIVISOR = 2147483647
FACTORS = (16807, 48271)
DIVISORS = (4, 8)

LOW_16_MASK = 0xFFFF


def parta(txt: str, loop_count: int = FOURTY_MILLION) -> int:
    return run(txt, loop_count)


def partb(txt: str, loop_count: int = FIVE_MILLION) -> int:
    return run(txt, loop_count, True)


def run(txt: str, loop_count: int, partb=False) -> int:
    seeds = tuple(int(line.split()[-1]) for line in txt.splitlines())
    args = (seeds, FACTORS, DIVISORS) if partb else (seeds, FACTORS)
    generators = tuple(create_generator(*a) for a in zip(*args))
    pairs = zip(*generators)
    return sum(a & LOW_16_MASK == b & LOW_16_MASK for a, b in itertools.islice(pairs, loop_count))


def create_generator(seed: int, factor: int, denominator: int = 1) -> Iterable[int]:
    n = seed
    while True:
        n *= factor
        n %= DIVISOR
        if denominator == 1 or n % denominator == 0:
            yield n


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
