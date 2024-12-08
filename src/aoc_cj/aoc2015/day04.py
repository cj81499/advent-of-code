import hashlib
import itertools


def find_hash(secret_key: str, zeros: int = 5) -> int:
    zeros_str = "0" * zeros
    return next(
        i for i in itertools.count() if hashlib.md5(f"{secret_key}{i}".encode()).hexdigest().startswith(zeros_str)
    )


def part_1(secret_key: str) -> int:
    return find_hash(secret_key)


def part_2(secret_key: str) -> int:
    return find_hash(secret_key, zeros=6)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
