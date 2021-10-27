def parse(line: str) -> tuple[str, str, int, int]:
    nums, letter, paswd = line.split(" ")
    return *map(int, nums.split("-")), letter[:-1], paswd


def helper(txt, fn):
    return sum(fn(*parse(line)) for line in txt.splitlines())


def parta(txt: str) -> int:
    return helper(txt, check_pass_a)


def check_pass_a(num_1, num_2, letter, paswd):
    return num_1 <= sum(map(lambda c: c == letter, paswd)) <= num_2


def partb(txt: str) -> int:
    return helper(txt, check_pass_b)


def check_pass_b(num_1, num_2, letter, paswd):
    return False if len(paswd) < num_2 else (letter == paswd[num_1 - 1]) ^ (letter == paswd[num_2 - 1])


def main(txt) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
