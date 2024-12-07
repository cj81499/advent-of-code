from string import ascii_lowercase


def get_group_of_people(txt):
    return [group.splitlines() for group in txt.split("\n\n")]


def part_1(txt):
    return sum(part_1_helper(group) for group in get_group_of_people(txt))


def part_1_helper(group):
    return len({c for person in group for c in person})


def part_2(txt):
    return sum(part_2_helper(group) for group in get_group_of_people(txt))


def part_2_helper(group):
    return len({letter for letter in ascii_lowercase if all(letter in person for person in group)})


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
