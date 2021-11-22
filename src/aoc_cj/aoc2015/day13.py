from itertools import permutations


def build_prefs(pref_str_list: list[str]) -> dict[str, dict[str, int]]:
    """Save attendee seating preferences"""
    prefs: dict[str, dict[str, int]] = {}

    # Save attendee preferences
    for pref in pref_str_list:
        name, _, impact, count, *_, neighbor = pref.split()

        happiness_change = int(count)
        if impact[0] == "l":
            happiness_change *= -1

        prefs.setdefault(name, {})
        prefs[name][neighbor[:-1]] = happiness_change

    return prefs


def attendee_happiness(attendee_prefs: dict[str, int], neighbors: set[str]):
    """Calculate happiness for an attendee with given neighbors"""
    return sum(attendee_prefs[n] for n in neighbors)


def attendee_neighbors(arangement, attendee_index):
    """Get neighbors of attendee in a given arangement"""
    return {arangement[attendee_index - 1], arangement[(attendee_index + 1) % len(arangement)]}


def seating_arangement_happiness(prefs, arangement):
    """Calculate happiness for a given seating arangement"""
    return sum(
        attendee_happiness(prefs[attendee], attendee_neighbors(arangement, i)) for i, attendee in enumerate(arangement)
    )


def optimal_happiness(prefs: dict[str, dict[str, int]]):
    """Calculate optimal happiness"""
    return max(seating_arangement_happiness(prefs, perm) for perm in permutations(prefs))


def add_self_to_prefs(prefs: dict[str, dict[str, int]]):
    """Add an apathetic individual named "Me" to prefs"""
    for attendee in prefs:
        prefs[attendee]["Me"] = 0
    prefs["Me"] = {neighbor: 0 for neighbor in prefs}
    return prefs


def parta(txt):
    return optimal_happiness(build_prefs(txt.splitlines()))


def partb(txt):
    return optimal_happiness(add_self_to_prefs(build_prefs(txt.splitlines())))


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
