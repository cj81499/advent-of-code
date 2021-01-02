import hashlib

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


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
