from collections import Counter

from more_itertools import pairwise


def parta(txt: str) -> int:
    polymer, rules = parse(txt)

    for _ in range(10):
        polymer = step(polymer, rules)

    c = Counter(polymer)
    return max(c.values()) - min(c.values())


def step(polymer: str, rules: dict[str, str]) -> str:
    new_polymer = [polymer[0]]
    for a, b in pairwise(polymer):
        new = rules[a + b]
        new_polymer.extend((new, b))
    return "".join(new_polymer)


def partb(txt: str) -> int:
    polymer, rules = parse(txt)

    pairs = Counter(pairwise(polymer))

    for _ in range(40):
        pairs_with_mid = ((a, rules[a + b], b, n) for (a, b), n in pairs.items())
        pairs = sum((Counter({(a, mid): n, (mid, b): n}) for a, mid, b, n in pairs_with_mid), Counter())

    # the first and last letter of final polymer are the same as in initial polymer
    # everything except for them will be double counted
    double_letter_counts = Counter((polymer[0], polymer[-1]))
    for (a, b), n in pairs.items():
        double_letter_counts[a] += n
        double_letter_counts[b] += n

    letter_counts = {n // 2 for n in double_letter_counts.values()}

    return max(letter_counts) - min(letter_counts)


def parse(txt: str) -> tuple[str, dict[str, str]]:
    polymer_template, pair_insertion_rules = txt.split("\n\n")
    return polymer_template, {k: v for k, v in (l.split(" -> ") for l in pair_insertion_rules.splitlines())}


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
