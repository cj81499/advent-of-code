def part1(nums: list):
    return sum(nums)


def part2(nums: list):
    seen_freqs = set()
    i = 0
    while True:
        for n in nums:
            seen_freqs.add(i)
            i += n
            if i in seen_freqs:
                return i


def main():
    _, input_lines = helpers.load_input(1, "Chronal Calibration")

    input_lines = [int(x) for x in input_lines]

    print(f"part1: {part1(input_lines)}")
    print(f"part2: {part2(input_lines)}")


if __name__ == "__main__":
    import helpers
    main()
