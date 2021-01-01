import hashlib
from datetime import date

import helpers

# TODO: Revisit? Slow.


def find_hash(secret_key: str, zeros: int):
    zeros_str = '0' * zeros
    i = 0
    while True:
        if hashlib.md5(f"{secret_key}{i}".encode("utf-8")).hexdigest().startswith(zeros_str):
            return i
        i += 1


def part1(secret_key: str):
    return find_hash(secret_key, 5)


def part2(secret_key: str):
    return find_hash(secret_key, 6)


def main():
    input_txt, _ = helpers.get_puzzle(date(2015, 12, 4), "The Ideal Stocking Stuffer")  # noqa

    print(f"part1: {part1(input_txt.strip())}")
    print(f"part2: {part2(input_txt.strip())}")


if __name__ == "__main__":
    main()
