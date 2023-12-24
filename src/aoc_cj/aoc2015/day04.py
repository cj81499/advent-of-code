import hashlib
import itertools


def find_hash(secret_key: str, zeros: int = 5):
    zeros_str = "0" * zeros
    for i in itertools.count():
        if hashlib.md5(f"{secret_key}{i}".encode()).hexdigest().startswith(zeros_str):
            return i


def part_1(secret_key: str):
    return find_hash(secret_key)


def part_2(secret_key: str):
    return find_hash(secret_key, zeros=6)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
