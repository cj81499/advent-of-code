def bag_rules(txt: str):
    rules = {}
    for line in txt.splitlines():
        if "no other bags." in line:
            rules[line.split(" bags")[0]] = None
        else:
            containing_bag, bag_contents = line.split(" bags contain ")
            bag_contents = bag_contents.strip(".").replace(" bags", "").replace(" bag", "").split(", ")
            rule_pairs = []
            for bag in bag_contents:
                first_space = bag.index(" ")
                rule_pairs.append(
                    (
                        int(bag[:first_space]),
                        bag[first_space + 1 :],
                    )
                )
            rules[containing_bag] = rule_pairs

    return rules


def can_hold_shiny_gold(rules, color):
    if color not in rules:
        return False
    rule = rules[color]
    if rule is None:
        return False
    for n, bag_color in rule:
        if bag_color == "shiny gold" or can_hold_shiny_gold(rules, bag_color):
            return True
    return False


def part_1(txt: str):
    rules = bag_rules(txt)
    return sum(can_hold_shiny_gold(rules, bag) for bag in rules)


def number_of_bags_inside_of(rules, color):
    if color not in rules:
        return 0
    rule = rules[color]
    if rule is None:
        return 0
    count = 0
    for n, bag_color in rule:
        count += n * (1 + number_of_bags_inside_of(rules, bag_color))
    return count


def part_2(txt: str):
    rules = bag_rules(txt)
    return number_of_bags_inside_of(rules, "shiny gold")


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
