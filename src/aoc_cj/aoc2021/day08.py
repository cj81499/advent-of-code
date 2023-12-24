import itertools

from more_itertools import bucket, one

SEGMENTS_IN_ONE = 2
SEGMENTS_IN_FOUR = 4
SEGMENTS_IN_SEVEN = 3
SEGMENTS_IN_EIGHT = 7


def part_1(txt: str) -> int:
    count = 0
    unique_segment_counts = {SEGMENTS_IN_ONE, SEGMENTS_IN_FOUR, SEGMENTS_IN_SEVEN, SEGMENTS_IN_EIGHT}
    for line in txt.splitlines():
        _signal_patterns, output_values = (x.split() for x in line.split(" | "))
        count += sum(len(output_value) in unique_segment_counts for output_value in output_values)
    return count


def part_2(txt: str) -> int:
    return sum(map(get_output_for_line, txt.splitlines()))


def get_output_for_line(line: str) -> int:
    signal_patterns, output_values = (x.split() for x in line.split(" | "))

    patterns = itertools.chain(signal_patterns, output_values)

    groups = bucket(patterns, key=len)
    patterns_by_length = {length: {"".join(sorted(pattern)) for pattern in groups[length]} for length in groups}

    one_pattern = one(patterns_by_length[SEGMENTS_IN_ONE])  # 1 is the only digit that uses 2 segments
    four_pattern = one(patterns_by_length[SEGMENTS_IN_FOUR])  # 4 is the only digit that uses 4 segments
    seven_pattern = one(patterns_by_length[SEGMENTS_IN_SEVEN])  # 7 is the only digit that uses 3 segments

    pattern_to_digit = {"abcdefg": 8, one_pattern: 1, four_pattern: 4, seven_pattern: 7}

    one_segments = set(one_pattern)
    four_segments = set(four_pattern)

    # 3 is the only digit that uses 5 segments and both of the segments on the right (the segments in 1)
    three_pattern = one(p for p in patterns_by_length[5] if all(x in p for x in one_segments))
    pattern_to_digit[three_pattern] = 3

    # 6 is the only digit that uses 6 segments and only one of the segments in digit 1
    six_pattern = one(p for p in patterns_by_length[6] if sum(x in p for x in one_segments) == 1)
    pattern_to_digit[six_pattern] = 6

    # 2 is the only digit that uses 5 segments and has 2 segments in common w/ 4
    two_pattern = one(p for p in patterns_by_length[5] if sum(x in p for x in four_segments) == 2)
    pattern_to_digit[two_pattern] = 2

    # 5 is the only remaining digit that uses 5 segments
    five_pattern = one(p for p in patterns_by_length[5] if p not in (two_pattern, three_pattern))
    pattern_to_digit[five_pattern] = 5

    # 9 is the only digit that uses 6 segments and has 4 segments in common w/ 4
    nine_pattern = one(p for p in patterns_by_length[6] if sum(x in p for x in four_segments) == 4)
    pattern_to_digit[nine_pattern] = 9

    # 0 is the only remaining digit that uses 6 segmensts
    zero_pattern = one(p for p in patterns_by_length[6] if p not in (six_pattern, nine_pattern))
    pattern_to_digit[zero_pattern] = 0

    output_digits = [pattern_to_digit["".join(sorted(output_value))] for output_value in output_values]
    return sum(10**i * n for i, n in enumerate(reversed(output_digits)))


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
