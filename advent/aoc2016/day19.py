from __future__ import annotations

import itertools

# Explanation: notice a pattern in the first few outputs (when they're still easy to compute)
# then, just keep the pattern going!


def parta(txt: str):
    def pattern():
        for i in itertools.count():
            yield from range(1, 2**i, 2)

    return next(itertools.islice(pattern(), int(txt) - 1, None))


def partb(txt: str):
    def pattern():
        for i in itertools.count():
            yield from (n for n in range(1, 3**i + 1) if n < 3**(i-1) or n % 2 != 0)

    return next(itertools.islice(pattern(), int(txt) - 1, None))


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
