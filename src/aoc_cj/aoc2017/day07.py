import re
from collections import Counter

import more_itertools as mi

REGEX = re.compile(r"([a-z]*) \((\d+)\)( -> (.*)|)")


class TreeNode:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.children: list[TreeNode] = []
        self.parent = None

    def add_child(self, child: "TreeNode"):
        assert child.parent is None
        child.parent = self
        self.children.append(child)

    @property
    def total_weight(self):
        return self.weight + sum(c.total_weight for c in self.children)

    def children_are_balanced(self):
        return len({c.total_weight for c in self.children}) == 1


def build_tree(txt: str) -> TreeNode:
    nodes: dict[str, TreeNode] = {}
    children: dict[str, tuple[str]] = {}

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


def part_1(txt):
    return build_tree(txt).name


def part_2(txt):
    traverse = build_tree(txt)
    while not traverse.children_are_balanced():
        total_weight_counts = Counter(c.total_weight for c in traverse.children)
        most_common_total_weight = total_weight_counts.most_common(n=1)[0][0]
        # next traverse node is the child with a unique total weight
        traverse = mi.one(c for c in traverse.children if c.total_weight != most_common_total_weight)

    child_weight = traverse.children[0].total_weight
    return most_common_total_weight - len(traverse.children) * child_weight


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
