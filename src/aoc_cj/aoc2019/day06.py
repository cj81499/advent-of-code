def get_masses(lines: list[str]) -> dict[str, str]:
    return {mass: parent for parent, mass in (line.split(")") for line in lines)}


def depth(masses: dict[str, str], mass: str) -> int:
    return len(ancestors(masses, mass))


def ancestors(masses: dict[str, str], mass: str) -> set[str]:
    parent = masses.get(mass)
    return set() if not parent else ancestors(masses, parent) | {parent}


def part_1(txt: str) -> int:
    lines = txt.splitlines()
    masses = get_masses(lines)
    return sum(depth(masses, m) for m in masses)


def part_2(txt: str) -> int:
    lines = txt.splitlines()
    masses = get_masses(lines)

    y_ancestors = ancestors(masses, "YOU")
    s_ancestors = ancestors(masses, "SAN")

    common_ancestors = y_ancestors & s_ancestors

    return len(y_ancestors) + len(s_ancestors) - 2 * len(common_ancestors)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
