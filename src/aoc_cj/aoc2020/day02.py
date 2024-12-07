def parse(line: str) -> tuple[str, str, int, int]:
    nums, letter, paswd = line.split(" ")
    return *map(int, nums.split("-")), letter[:-1], paswd


def helper(txt, fn):
    return sum(fn(*parse(line)) for line in txt.splitlines())


def part_1(txt: str) -> int:
    return helper(txt, check_pass_1)


def check_pass_1(num_1, num_2, letter, paswd):
    return num_1 <= sum(map(lambda c: c == letter, paswd)) <= num_2


def part_2(txt: str) -> int:
    return helper(txt, check_pass_2)


def check_pass_2(num_1, num_2, letter, paswd):
    return False if len(paswd) < num_2 else (letter == paswd[num_1 - 1]) ^ (letter == paswd[num_2 - 1])


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
