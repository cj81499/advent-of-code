def is_valid(passphrase: str):
    words = passphrase.split()
    return len(set(words)) == len(words)


def parta(txt):
    return sum(is_valid(passphrase) for passphrase in txt.splitlines())


def is_valid_b(passphrase: str):
    words = passphrase.split()
    words = ["".join(sorted(word)) for word in words]
    return len(set(words)) == len(words)


def partb(txt):
    return sum(is_valid_b(passphrase) for passphrase in txt.splitlines())


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
