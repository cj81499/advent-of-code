import hashlib
from datetime import date

# TODO: Revisit? Slow.


def find_hash(secret_key: str, zeros: int):
    zeros_str = '0' * zeros
    i = 0
    while True:
        if hashlib.md5(f"{secret_key}{i}".encode("utf-8")).hexdigest().startswith(zeros_str):
            return i
        i += 1


def parta(secret_key: str):
    return find_hash(secret_key, 5)


def partb(secret_key: str):
    return find_hash(secret_key, 6)


def main():
    input_txt, _ = helpers.get_puzzle(date(2015, 12, 4), "The Ideal Stocking Stuffer")  # noqa

    print(f"parta: {parta(input_txt.strip())}")
    print(f"partb: {partb(input_txt.strip())}")


if __name__ == "__main__":
    main()
