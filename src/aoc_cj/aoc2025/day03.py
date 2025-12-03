def max_joltage(battery_bank: str, *, width: int = 2) -> int:
    """
    Find the maximum joltage of a given width for a given battery bank.

    For each digit in the result, we will use the first occurrence of the
    greatest available digit. We will take care to leave enough digits for the
    remaining width.

    For example, to find the max joltage of width 3 for 1497038, we do the
    following:

    1. Consider 14970. We start at the beginning of the battery bank. We ignore
       38 because there are still two digits after this one, so choosing either
       of those digits would not leave enough remaining digits to build a
       joltage of width 3. The greatest available digit is 9.
    2. Consider 703. We start after the 9 we chose for the previous digit.
       We ignore 8 because there is still one digit after this one, so
       choosing it would not leave enough remaining digits. The greatest
       available digit is 7.
    3. Consider 038. We start after the 7 we chose for the previous digit.
       We don't ignore anything because this is the last digit. The greatest
       available digit is 8.

    Thus, the max joltage of width 3 for 1497038 is 978
    """

    digits = []

    start = 0
    # do not consider digits beyond `end` or there won't be enough digits for the full width
    for end in range(len(battery_bank) - width + 1, len(battery_bank) + 1):
        max_digit = max(battery_bank[start:end])
        digits.append(max_digit)
        # remaining digits must come after the one we chose
        start = battery_bank.index(max_digit, start, end) + 1

    return int("".join(digits))


def part_1(txt: str) -> int:
    return sum(max_joltage(battery_bank) for battery_bank in txt.splitlines())


def part_2(txt: str) -> int:
    return sum(max_joltage(battery_bank, width=12) for battery_bank in txt.splitlines())


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
