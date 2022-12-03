from collections import defaultdict

from lark import Lark


def parse_replacements(txt):
    replacements = defaultdict(set)
    for line in txt.splitlines():
        from_atom, to_molecule = line.split(" => ")
        replacements[from_atom].add(to_molecule)
    return replacements


def split_molecule_into_atoms(molecule: str):
    atoms = []
    start = 0
    for i, c in enumerate(molecule):
        if c.isupper():
            if i != start:
                atoms.append(molecule[start:i])
            start = i
    atoms.append(molecule[start:])
    return atoms


def parta(txt):
    replacements, medicine = txt.split("\n\n")
    replacements = parse_replacements(replacements)
    medicine_atoms = split_molecule_into_atoms(medicine)
    distinct_molecules = set()
    new_molecule_atoms = medicine_atoms.copy()
    for i, atom in enumerate(medicine_atoms):
        for replacement in replacements[atom]:
            new_molecule_atoms[i] = replacement
            distinct_molecules.add("".join(new_molecule_atoms))
        new_molecule_atoms[i] = atom  # reset new_molecule_atoms for next loop
    return len(distinct_molecules)


def is_leaf(node):
    return len(node.children) == 0


def leaf_count(tree):
    return 1 if is_leaf(tree) else sum(leaf_count(c) for c in tree.children)


def node_count(tree):
    return 1 + sum(node_count(c) for c in tree.children)


def partb(txt):
    """
    https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4p1td?utm_source=share&utm_medium=web2x&context=3
    "this is actually the production rules for an unambiguous grammar"
    """
    replacements, medicine = txt.split("\n\n")
    replacements = parse_replacements(replacements)
    replacements = {k: [split_molecule_into_atoms(v) for v in vals] for k, vals in replacements.items()}

    all_atoms = set()
    for from_atom, to_molecules in replacements.items():
        all_atoms.add(from_atom)
        for m in to_molecules:
            all_atoms.update(m)

    # convert replacements into a grammar (for Lark)
    rules = []
    for atom in all_atoms:
        rule_parts = []
        if atom in replacements:
            for m in replacements[atom]:
                rule_parts.append(" ".join(a.lower() for a in m))  # rule names must be lowercase
        if atom != "e":
            rule_parts.append(f'"{atom}"')  # add terminal
        rule_parts = " | ".join(rule_parts)
        rules.append(f"{atom.lower()}: {rule_parts}")
    grammar = "\n".join(rules)

    # parse the medicine string using the grammar
    parser = Lark(grammar, start="e")
    tree = parser.parse(medicine)

    # the number of transforms is the number of non-leaf nodes
    return node_count(tree) - leaf_count(tree)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
