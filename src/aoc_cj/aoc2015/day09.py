import itertools
from typing import Self, override


class Location:
    def __init__(self, name: str) -> None:
        self.name = name
        self.distances: dict[str, int] = {}

    def set_dist_between(self, other_loc_name: str, dist: int) -> None:
        self.distances[other_loc_name] = dist

    def get_dist_between(self, other: Self) -> int:
        assert isinstance(other, Location)
        if other.name in self.distances:
            return self.distances[other.name]
        if self.name in other.distances:
            return other.distances[self.name]
        msg = "unreachable"
        raise AssertionError(msg)

    @override
    def __repr__(self) -> str:
        return f"{self.name} {self.distances}"


def find_paths(lines: list[str]) -> tuple[float, int]:
    # Save locations and the distances between them
    locations: dict[str, Location] = {}
    for line in lines:
        location_a, _, location_b, _, dist = line.split()
        dist = int(dist)
        locations.setdefault(location_a, Location(location_a))
        locations.setdefault(location_b, Location(location_b))
        # We only need to save the distance info to one location object.
        locations[location_a].set_dist_between(location_b, dist)

    min_dist = float("inf")
    max_dist = 0
    # Generate and "walk" each path
    for path in itertools.permutations(locations):
        dist = 0
        prev_loc: str | None = None
        for loc in path:
            if prev_loc:
                dist += locations[loc].get_dist_between(locations[prev_loc])
            prev_loc = loc

        min_dist = min(min_dist, dist)
        max_dist = max(max_dist, dist)
    return min_dist, max_dist


def part_1(txt: str) -> float:
    return find_paths(txt.splitlines())[0]


def part_2(txt: str) -> int:
    return find_paths(txt.splitlines())[1]


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
