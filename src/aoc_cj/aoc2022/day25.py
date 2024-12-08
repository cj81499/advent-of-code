_SNAFU_TO_BASE_10 = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}


def snafu_to_base_10(snafu: str) -> int:
    return sum(5**i * _SNAFU_TO_BASE_10[c] for i, c in enumerate(reversed(snafu)))


def base_10_to_snafu(n: int) -> str:
    n, rem = divmod(n, 5)
    last_digit = "012=-"[rem]
    if rem > 2:
        return base_10_to_snafu(n + 1) + last_digit
    if n == 0:
        return last_digit
    return base_10_to_snafu(n) + last_digit


def part_1(txt: str) -> str:
    return base_10_to_snafu(sum(map(snafu_to_base_10, txt.splitlines())))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
