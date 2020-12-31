import collections  # noqa
import itertools  # noqa
import re  # noqa
from dataclasses import dataclass


@dataclass
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


def parta(txt):
    claims = [Claim.parse(line) for line in txt.splitlines()]
    grid = build_grid(claims)
    return sum(len(c) > 1 for p, c in grid.items())


def no_overlap(grid, claim):
    for y in range(claim.height):
        for x in range(claim.width):
            if len(grid[(claim.x + x, claim.y + y)]) > 1:
                return False
    return True


def partb(txt):
    claims = [Claim.parse(line) for line in txt.splitlines()]
    grid = build_grid(claims)
    return next(c for c in claims if no_overlap(grid, c)).claim_id


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
