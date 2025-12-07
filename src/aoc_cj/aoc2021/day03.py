from collections import Counter
from collections.abc import Callable


def part_1(txt: str) -> int:
    gamma_rate = 0
    epsilon_rate = 0

    for column in zip(*txt.splitlines(), strict=True):
        c = Counter(column)
        gamma_rate = (gamma_rate << 1) | int(most_common(c))
        epsilon_rate = (epsilon_rate << 1) | int(least_common(c))

    return gamma_rate * epsilon_rate


def part_2(txt: str) -> int:
    numbers = txt.splitlines()

    oxygen_generator_rating = bitwise_filter(numbers, most_common)
    c02_scrubber_rating = bitwise_filter(numbers, least_common)

    return oxygen_generator_rating * c02_scrubber_rating


def most_common(c: Counter[str]) -> str:
    """Pick most common between 0 and 1, break ties w/ 1."""

    return "0" if c["0"] > c["1"] else "1"


def least_common(c: Counter[str]) -> str:
    """Pick least common between 0 and 1, break ties w/ 0."""

    return "1" if c["1"] < c["0"] else "0"


def bitwise_filter(numbers: list[str], choose_to_keep: Callable[[Counter[str]], str], i: int = 0) -> int:
    if len(numbers) == 1:  # if there is only one number left, we're done!
        return int(numbers[0], 2)
    to_keep = choose_to_keep(Counter(s[i] for s in numbers))  # pick which digit (0 or 1) to keep
    filtered = [n for n in numbers if n[i] == to_keep]  # keep only numbers where the i-th digit is to_keep
    return bitwise_filter(filtered, choose_to_keep, i + 1)  # keep going!


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
