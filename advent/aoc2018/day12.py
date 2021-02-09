from __future__ import annotations

FIFTY_BILLION = 50_000_000_000


def parta(txt: str):
    return simulate_plant_growth(txt)


def partb(txt: str):
    return simulate_plant_growth(txt, generations=FIFTY_BILLION)


def view(pots, center):
    return "".join(("#" if i in pots else ".") for i in range(center - 2, center + 3))


def next_pots(pots, rules):
    return {
        c for c in range(min(pots) - 2, max(pots) + 3)
        if view(pots, c) in rules
    }


def simulate_plant_growth(txt: str, generations=20):
    initial_state, rules = txt.split("\n\n")
    initial_state = initial_state.lstrip("initial state:")
    initial_state = {i for i, c in enumerate(initial_state) if c == "#"}
    # set of rules that produce pots
    rules = {k for k, v in (line.split(" => ") for line in rules.splitlines()) if v == "#"}

    # The rate at which the sum of pot numbers changes eventually becomes stable.
    # Once we've detected this, we can skip the rest of the simulation.
    pots = initial_state
    prev_sum = sum(pots)
    prev_change_in_sum = None
    repeat_change_count = 0
    for i in range(generations):
        pots = next_pots(pots, rules)
        s = sum(pots)
        change_in_sum = s - prev_sum
        if change_in_sum != prev_change_in_sum:
            repeat_change_count = 0
        else:
            repeat_change_count += 1
            if repeat_change_count > 10:
                return prev_sum + (FIFTY_BILLION - i) * change_in_sum
        prev_sum = s
        prev_change_in_sum = change_in_sum

    return sum(pots)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
