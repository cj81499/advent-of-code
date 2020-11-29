from typing import Dict, List, Set

from aocd import data


def get_masses(lines: List[str]) -> Dict[str, str]:
    return {mass: parent for parent, mass in (l.split(")") for l in lines)}


def depth(masses: Dict[str, str], mass: str) -> int:
    return len(ancestors(masses, mass))


def ancestors(masses: Dict[str, str], mass: str) -> Set[str]:
    parent = masses.get(mass)
    return set() if not parent else ancestors(masses, parent) | {parent}


def parta(txt: str) -> int:
    lines = txt.splitlines()
    masses = get_masses(lines)
    return sum(depth(masses, m) for m in masses)


def partb(txt: str) -> int:
    lines = txt.splitlines()
    masses = get_masses(lines)

    y_ancestors = ancestors(masses, "YOU")
    s_ancestors = ancestors(masses, "SAN")

    common_ancestors = y_ancestors & s_ancestors

    return len(y_ancestors) + len(s_ancestors) - 2 * len(common_ancestors)


def main() -> None:


    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")


if __name__ == "__main__":
    main()
