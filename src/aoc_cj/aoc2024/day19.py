import functools


def design_is_possible(design: str, available_patterns: frozenset[str]) -> bool:
    if design == "":
        return True
    for p in available_patterns:
        if design.startswith(p):
            if design_is_possible(design.removeprefix(p), available_patterns):
                return True
    return False


@functools.cache
def ways_design_is_possible(design: str, available_patterns: frozenset[str]) -> int:
    if design == "":
        return 1
    return sum(
        ways_design_is_possible(design.removeprefix(p), available_patterns)
        for p in available_patterns
        if design.startswith(p)
    )


def part_1(txt: str) -> int:
    available_patterns, desired_designs = txt.split("\n\n")
    available_patterns = frozenset(available_patterns.split(", "))
    desired_designs = desired_designs.splitlines()
    return sum(1 for d in desired_designs if design_is_possible(d, available_patterns))


def part_2(txt: str) -> int:
    available_patterns, desired_designs = txt.split("\n\n")
    available_patterns = frozenset(available_patterns.split(", "))
    desired_designs = desired_designs.splitlines()
    return sum(ways_design_is_possible(d, available_patterns) for d in desired_designs)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
