from __future__ import annotations

import re
from collections import Counter
from typing import Dict, List, Tuple

REGEX = re.compile(r"([a-z]*) \((\d+)\)( -> (.*)|)")


class TreeNode:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.children: List[TreeNode] = []
        self.parent = None

    def add_child(self, child: TreeNode):
        assert child.parent is None
        child.parent = self
        self.children.append(child)

    @property
    def total_weight(self):
        return self.weight + sum(c.total_weight for c in self.children)

    def children_are_balanced(self):
        return len(set(c.total_weight for c in self.children)) == 1


def build_tree(txt: str) -> TreeNode:
    nodes: Dict[str, TreeNode] = {}
    children: Dict[str, Tuple[str]] = {}

    for line in txt.splitlines():
        name, num, _, children_str = REGEX.match(line).groups()
        nodes[name] = TreeNode(name, int(num))
        children[name] = tuple() if children_str is None else tuple(children_str.split(", "))

    for name, children_tuple in children.items():
        for child in children_tuple:
            nodes[name].add_child(nodes[child])

    traverse = nodes[name]
    while traverse.parent is not None:
        traverse = traverse.parent

    return traverse


def parta(txt):
    return build_tree(txt).name


def partb(txt):
    traverse = build_tree(txt)
    while not traverse.children_are_balanced():
        total_weight_counts = Counter(c.total_weight for c in traverse.children)
        most_common_total_weight = total_weight_counts.most_common(n=1)[0][0]
        # next traverse node is the child with a unique total weight
        traverse = [c for c in traverse.children if c.total_weight != most_common_total_weight][0]

    child_weight = traverse.children[0].total_weight
    return most_common_total_weight - len(traverse.children) * child_weight


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
