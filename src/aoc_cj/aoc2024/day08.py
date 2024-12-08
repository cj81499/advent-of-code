import itertools

import more_itertools as mi


def part_1(txt: str) -> int:
    lines = txt.splitlines()
    scan = {x + y * 1j: c for y, row in enumerate(lines) for x, c in enumerate(row)}
    antennas_by_freq = mi.bucket(scan.keys(), key=lambda p: scan[p], validator=lambda k: k != ".")

    antinodes_locations = set[complex]()
    for freq in antennas_by_freq:
        antenna_locations = list(antennas_by_freq[freq])
        for a, b in itertools.combinations(antenna_locations, 2):
            diff = a - b
            antinodes_locations.add(a + diff)
            antinodes_locations.add(b - diff)

    # filter out antinodes that ar outiside the scan
    return len(antinodes_locations.intersection(scan))


def part_2(txt: str) -> int:
    lines = txt.splitlines()
    height = len(lines)
    width = len(lines[0])

    scan = {x + y * 1j: c for y, row in enumerate(lines) for x, c in enumerate(row)}
    antennas_by_freq = mi.bucket(scan.keys(), key=lambda p: scan[p], validator=lambda k: k != ".")

    antinodes_locations = set[complex]()
    for freq in antennas_by_freq:
        antenna_locations = list(antennas_by_freq[freq])
        for a, b in itertools.combinations(antenna_locations, 2):
            diff = a - b
            # HACK: 100 is probably enough....
            # should probably do this by going until the antinode is "out of bounds"
            for i in range(100):
                antinodes_locations.add(a + i * diff)
                antinodes_locations.add(b - i * diff)

    return len(antinodes_locations.intersection(scan))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
