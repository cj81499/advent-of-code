import itertools


class Location:
    def __init__(self, name):
        self.name = name
        self.distances = {}

    def set_dist_between(self, other_loc_name: str, dist: int):
        self.distances[other_loc_name] = dist

    def get_dist_between(self, other):
        assert isinstance(other, Location)
        if other.name in self.distances:
            return self.distances[other.name]
        elif self.name in other.distances:
            return other.distances[self.name]
        assert False, "unreachable"

    def __repr__(self) -> str:
        return f"{self.name} {self.distances}"


def find_paths(lines: list):
    # Save locations and the distances between them
    locations: dict[str, Location] = {}
    for line in lines:
        locA, _, locB, _, dist = line.split()
        dist = int(dist)
        locations.setdefault(locA, Location(locA))
        locations.setdefault(locB, Location(locB))
        # We only need to save the distance info to one location object.
        locations[locA].set_dist_between(locB, dist)

    min_dist = float("inf")
    max_dist = 0
    # Generate and "walk" each path
    for path in itertools.permutations(locations):
        dist = 0
        prev_loc = None
        for loc in path:
            if prev_loc:
                dist += locations[loc].get_dist_between(locations[prev_loc])
            prev_loc = loc

        min_dist = min(min_dist, dist)
        max_dist = max(max_dist, dist)
    return min_dist, max_dist


def parta(txt):
    return find_paths(txt.splitlines())[0]


def partb(txt):
    return find_paths(txt.splitlines())[1]


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
