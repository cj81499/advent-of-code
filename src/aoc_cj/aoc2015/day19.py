import dataclasses
import itertools
import re

import lark
import more_itertools as mi

ELEMENT_PATTERN = re.compile(r"[A-Z][a-z]*")


@dataclasses.dataclass(frozen=True)
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


def part_1(txt: str) -> int:
    replacements, medicine_molecule = parse(txt)
    medicine_elements = ELEMENT_PATTERN.findall(medicine_molecule)
    molecules = {
        "".join((*medicine_elements[:i], r.output_molecule, *medicine_elements[i + 1 :]))
        for (i, element), r in itertools.product(enumerate(medicine_elements), replacements)
        if r.input == element
    }
    return len(molecules)


def part_2(txt: str) -> int:
    """
    https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4p1td/?utm_source=share&utm_medium=web2x&context=3
    "this is actually the production rules for an unambiguous grammar"
    so let's generate one and parse the molecule!
    """
    replacements, medicine_molecule = parse(txt)

    buckets = mi.bucket(replacements, key=lambda r: r.input)
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
    node_count = mi.ilen(tree.find_pred(lambda _: True))
    leaf_count = mi.ilen(tree.find_pred(lambda t: len(t.children) == 0))
    return node_count - leaf_count


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
