import collections
import dataclasses
import re


@dataclasses.dataclass
class Claim:
    claim_id: int
    x: int
    y: int
    width: int
    height: int

    _PARSE_REGEX = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

    @staticmethod
    def parse(claim: str):
        match = Claim._PARSE_REGEX.match(claim)
        nums = map(int, match.groups())
        return Claim(*nums)


def build_grid(claims):
    grid = collections.defaultdict(set)

    for c in claims:
        for y in range(c.height):
            for x in range(c.width):
                grid[(c.x + x, c.y + y)].add(c.claim_id)

    return grid


def part_1(txt):
    claims = [Claim.parse(line) for line in txt.splitlines()]
    grid = build_grid(claims)
    return sum(len(c) > 1 for p, c in grid.items())


def no_overlap(grid, claim):
    for y in range(claim.height):
        for x in range(claim.width):
            if len(grid[(claim.x + x, claim.y + y)]) > 1:
                return False
    return True


def part_2(txt):
    claims = [Claim.parse(line) for line in txt.splitlines()]
    grid = build_grid(claims)
    return next(c for c in claims if no_overlap(grid, c)).claim_id


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
