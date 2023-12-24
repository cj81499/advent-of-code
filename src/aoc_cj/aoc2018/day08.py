def sum_all_meta_entries(tokens):
    child_count = tokens.pop(0)
    meta_entries = tokens.pop(0)
    sum_of_meta = 0
    for _ in range(child_count):
        sum_of_meta += sum_all_meta_entries(tokens)
    for _ in range(meta_entries):
        sum_of_meta += tokens.pop(0)
    return sum_of_meta


def part_1(txt):
    tokens = list(map(int, txt.split()))
    return sum_all_meta_entries(tokens)


def node_value(tokens):
    child_count = tokens.pop(0)
    meta_entries = tokens.pop(0)
    children = []
    for _ in range(child_count):
        children.append(node_value(tokens))
    value = 0
    if len(children) == 0:
        for _ in range(meta_entries):
            value += tokens.pop(0)
    else:
        for _ in range(meta_entries):
            i = tokens.pop(0) - 1
            if i < len(children):
                value += children[i]
    return value


def part_2(txt):
    tokens = list(map(int, txt.split()))
    return node_value(tokens)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
