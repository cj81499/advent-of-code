import numpy as np
import parse


class Claim:
    p = parse.compile("#{:d} @ {:d},{:d}: {:d}x{:d}")

    gridA = np.zeros((1000, 1000), dtype=int)
    count = 0

    gridB = np.zeros((1000, 1000), dtype=int)
    validity = []

    def __init__(self, s: str):
        self.claim_id, self.left, self.top, self.width, self.height = Claim.p.parse(s)
        Claim.validity.append(True)

    def parta(self):
        for y in range(self.top, self.top + self.height):
            for x in range(self.left, self.left + self.width):
                Claim.gridA[y, x] += 1
                if Claim.gridA[y, x] == 2:
                    Claim.count += 1

    def partb(self):
        for y in range(self.top, self.top + self.height):
            for x in range(self.left, self.left + self.width):
                if Claim.gridB[y, x] != 0:
                    Claim.validity[self.claim_id - 1] = False
                    Claim.validity[Claim.gridB[y, x] - 1] = False
                Claim.gridB[y, x] = self.claim_id


def parta(txt):
    claims = [Claim(s) for s in txt.splitlines()]
    for c in claims:
        c.parta()
    return Claim.count


def partb(txt):
    claims = [Claim(s) for s in txt.splitlines()]
    for c in claims:
        c.partb()
    return Claim.validity.index(True) + 1


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
