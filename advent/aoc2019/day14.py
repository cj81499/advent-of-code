from aocd import data


class Chemical():
    def __init__(self, chem_str: str) -> None:
        qty, self.name = chem_str.split(" ")
        self.qty = int(qty)

    def __repr__(self) -> str:
        return f"{self.qty} {self.name}"


class Reaction():
    def __init__(self, rxn_str: str) -> None:
        input_chems_str, output_chem_str = rxn_str.split(" => ")
        self.output = Chemical(output_chem_str)
        self.inputs = {Chemical(c) for c in input_chems_str.split(", ")}

    def __repr__(self) -> str:
        return f"{', '.join(str(i) for i in self.inputs)} => {self.output}"


def parse_reactions(lines: list[str]) -> set[Reaction]:
    return {Reaction(line) for line in lines}


def ore_req(
    chemical: str, rxns: set[Reaction], count: int = 1,
    leftover=None
) -> int:
    # inspired by u/tinyhurricanes' solution
    # https://www.reddit.com/r/adventofcode/comments/eafj32/2019_day_14_solutions/fax5izj
    if chemical == "ORE":
        return count
    if leftover is None:
        leftover = {}
    rxn = next(filter(lambda rxn: rxn.output.name == chemical, rxns))
    existing = leftover.get(chemical, 0)
    from math import ceil
    mult = ceil(max(count - existing, 0) / rxn.output.qty)
    unused = rxn.output.qty * mult - (count - existing)
    leftover[chemical] = unused
    return sum(
        ore_req(i.name, rxns, mult * i.qty, leftover) for i in rxn.inputs
    )


def parta(txt: str) -> int:
    lines = txt.splitlines()

    rxns = parse_reactions(lines)
    return ore_req("FUEL", rxns)


def partb(txt: str) -> int:
    lines = txt.splitlines()

    ORE_QTY = 1000000000000
    rxns = parse_reactions(lines)

    # Binary search
    high = ORE_QTY
    low = 0
    while high - low > 1:
        mid = (high + low) // 2
        if ore_req("FUEL", rxns, mid) < ORE_QTY:
            low = mid
        else:
            high = mid
    return low


def main() -> None:
    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")


if __name__ == "__main__":
    main()
