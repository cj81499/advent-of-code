def is_valid_1(passphrase: str):
    words = passphrase.split()
    return len(set(words)) == len(words)


def part_1(txt):
    return sum(is_valid_1(passphrase) for passphrase in txt.splitlines())


def is_valid_2(passphrase: str):
    words = passphrase.split()
    words = ["".join(sorted(word)) for word in words]
    return len(set(words)) == len(words)


def part_2(txt):
    return sum(is_valid_2(passphrase) for passphrase in txt.splitlines())


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
