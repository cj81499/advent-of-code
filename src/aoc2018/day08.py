def sum_all_meta_entries(tokens):
    child_count = tokens.pop(0)
    meta_entries = tokens.pop(0)
    sum_of_meta = 0
    for _ in range(child_count):
        sum_of_meta += sum_all_meta_entries(tokens)
    for _ in range(meta_entries):
        sum_of_meta += tokens.pop(0)
    return sum_of_meta


def parta(txt):
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


def partb(txt):
    tokens = list(map(int, txt.split()))
    return node_value(tokens)


def main():
    input_txt, _ = helpers.load_input(8, "Memory Maneuver")

    print(f"parta: {parta(input_txt)}")
    print(f"partb: {partb(input_txt)}")


if __name__ == "__main__":
    import helpers
    main()
