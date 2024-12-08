import itertools

import more_itertools as mi


def part_1(txt: str) -> int:
    scan, antennas_by_freq = parse(txt)

    antinode_locations = set[complex]()
    for freq in antennas_by_freq:
        for a, b in itertools.combinations(antennas_by_freq[freq], 2):
            diff = a - b
            antinode_locations.add(a + diff)
            antinode_locations.add(b - diff)

    # count antinodes that are within the scan
    return len(antinode_locations.intersection(scan))


def part_2(txt: str) -> int:
    scan, antennas_by_freq = parse(txt)
    lines = txt.splitlines()
    max_h_w = max(len(lines), len(lines[0]))

    antinode_locations = set[complex]()
    for freq in antennas_by_freq:
        for a, b in itertools.combinations(antennas_by_freq[freq], 2):
            diff = a - b
            # find "resonant" antinodes
            # max_h_w is guaranteed to be enough "steps", even if two nodes w/ the same freq are immediately next to
            # one another.
            # Another approach would be to start at each node and "walk `diff` steps" until the position of the antinode
            # is outside the scan. This is (slightly) simpler to implement and perf is not an issue.
            antinode_locations.update(a + i * diff for i in range(max_h_w))
            antinode_locations.update(b - i * diff for i in range(max_h_w))

    # count antinodes that are within the scan
    return len(antinode_locations.intersection(scan))


def parse(txt: str) -> tuple[dict[complex, str], "mi.bucket[complex, str]"]:
    scan = {x + y * 1j: c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row)}
    antennas_by_freq = mi.bucket(scan.keys(), key=lambda p: scan[p], validator=lambda k: k != ".")
    return scan, antennas_by_freq


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
