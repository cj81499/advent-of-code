import itertools
import re
from dataclasses import dataclass

import lark
from more_itertools import bucket

ELEMENT_PATTERN = re.compile(r"[A-Z][a-z]*")


@dataclass(frozen=True)
class Replacement:
    input: str
    output_molecule: str
    output_elements: tuple[str]

    @staticmethod
    def parse(txt: str) -> "Replacement":
        left, right = txt.split(" => ")
        return Replacement(left, right, tuple(ELEMENT_PATTERN.findall(right)))


def parse(txt: str) -> tuple[set[Replacement], str]:
    replacements, medicine_molecule = txt.split("\n\n")
    return {Replacement.parse(r) for r in replacements.splitlines()}, medicine_molecule


def parta(txt: str) -> int:
    replacements, medicine_molecule = parse(txt)
    medicine_elements = ELEMENT_PATTERN.findall(medicine_molecule)
    molecules = {
        "".join((*medicine_elements[:i], r.output_molecule, *medicine_elements[i + 1 :]))
        for (i, element), r in itertools.product(enumerate(medicine_elements), replacements)
        if r.input == element
    }
    return len(molecules)


def leaf_count(tree: lark.Tree) -> int:
    return 1 if len(tree.children) == 0 else 0 + sum(map(leaf_count, tree.children))


def node_count(tree: lark.Tree):
    return 1 + sum(map(node_count, tree.children))


def partb(txt: str) -> None:
    """
    https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4p1td/?utm_source=share&utm_medium=web2x&context=3
    "this is actually the production rules for an unambiguous grammar"
    so let's generate one and parse the molecule!
    """
    replacements, medicine_molecule = parse(txt)

    buckets = bucket(replacements, key=lambda r: r.input)
    replacements_by_input = {i: set(buckets[i]) for i in buckets}

    all_elements = {
        *(r.input for r in replacements),
        *itertools.chain.from_iterable(r.output_elements for r in replacements),
    }

    # create a lark grammar
    rules = []
    for element in all_elements:
        rule_parts = [
            *(" ".join(e.lower() for e in rep.output_elements) for rep in replacements_by_input.get(element, set())),
            f'"{element}"',
        ]
        rules.append(f"{element.lower()}: {' | '.join(rule_parts)}")
    grammar = "\n".join(rules)

    # parse the medicine
    parser = lark.Lark(grammar, start="e")
    tree = parser.parse(medicine_molecule)

    # the number of transforms is the number of non-leaf nodes
    return node_count(tree) - leaf_count(tree)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
