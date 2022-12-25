_SNAFU_TO_BASE_10 = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}


def snafu_to_base_10(snafu: str) -> int:
    result = 0
    base = 1
    for c in reversed(snafu):
        result += base * _SNAFU_TO_BASE_10[c]
        base *= 5
    return result


def numberToBase(n: int, base: int) -> list[int]:
    if n == 0:
        return [0]
    digits: list[int] = []
    while n:
        n, rem = divmod(n, base)
        digits.append(rem)
    return digits[::-1]


def base_10_to_snafu(n: int) -> str:
    base_5 = numberToBase(n, 5)
    rev_base_5 = list(reversed(base_5))

    snafu: list[str] = []
    i = 0
    while i < len(rev_base_5):
        n_at_i = rev_base_5[i]
        snafu.append(["0", "1", "2", "=", "-"][n_at_i])
        if n_at_i > 2:
            j = i + 1
            if j <= len(rev_base_5):
                rev_base_5.append(0)
            rev_base_5[j] += 1
            while rev_base_5[j] == 5:
                rev_base_5[j] = 0
                j += 1
                if j <= len(rev_base_5):
                    rev_base_5.append(0)
                rev_base_5[j] += 1
        i += 1

    return "".join(reversed(snafu)).lstrip("0")


def parta(txt: str) -> str:
    return base_10_to_snafu(sum(map(snafu_to_base_10, txt.splitlines())))


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
