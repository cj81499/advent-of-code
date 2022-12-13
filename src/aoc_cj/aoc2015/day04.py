import hashlib
import itertools


def find_hash(secret_key: str, zeros: int = 5):
    zeros_str = "0" * zeros
    for i in itertools.count():
        if hashlib.md5(f"{secret_key}{i}".encode()).hexdigest().startswith(zeros_str):
            return i


def parta(secret_key: str):
    return find_hash(secret_key)


def partb(secret_key: str):
    return find_hash(secret_key, zeros=6)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
