"""cj's utilities https://adventofcode.com/"""


def clamp(n: int, min_n: int, max_n: int) -> int:
    assert min_n <= max_n
    return max(min_n, min(n, max_n))
