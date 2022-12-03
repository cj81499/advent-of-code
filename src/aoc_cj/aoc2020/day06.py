from string import ascii_lowercase


def get_group_of_people(txt):
    return [group.splitlines() for group in txt.split("\n\n")]


def parta(txt):
    return sum(parta_helper(group) for group in get_group_of_people(txt))


def parta_helper(group):
    return len({c for person in group for c in person})


def partb(txt):
    return sum(partb_helper(group) for group in get_group_of_people(txt))


def partb_helper(group):
    return len({letter for letter in ascii_lowercase if all(letter in person for person in group)})


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
