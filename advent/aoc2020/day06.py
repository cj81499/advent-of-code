from string import ascii_lowercase


def get_group_of_people(txt):
    return [group.splitlines() for group in txt.split("\n\n")]


def parta(txt):
    return sum(parta_helper(group) for group in get_group_of_people(txt))


def parta_helper(group):
    return len(set(c for person in group for c in person))


def partb(txt):
    return sum(partb_helper(group) for group in get_group_of_people(txt))


def partb_helper(group):
    return len(set(letter for letter in ascii_lowercase if all(letter in person for person in group)))


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
