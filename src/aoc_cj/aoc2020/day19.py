class Option:
    def __init__(self, option_str):
        self.parts = [int(o) if o.isnumeric() else o.strip('"') for o in option_str.split()]

    def __repr__(self):
        return f"Option(parts={self.parts})"

    @staticmethod
    def _matches_helper(message, rules, remaining_parts):
        if len(remaining_parts) == 0:
            yield 0
            return
        first, *rest = remaining_parts
        if isinstance(first, str):
            if message.startswith(first):
                for m in Option._matches_helper(message[len(first) :], rules, rest):
                    yield len(first) + m
        elif isinstance(first, int):
            for m1 in rules[first]._matches(message, rules):
                for m2 in Option._matches_helper(message[m1:], rules, rest):
                    yield m1 + m2
        else:
            raise Exception("unreachable")

    def _matches(self, message, rules):
        return Option._matches_helper(message, rules, [*self.parts])


class Rule:
    def __init__(self, rule_str):
        n, options = rule_str.split(": ")
        self.n = int(n)
        self.options = [Option(o) for o in options.split(" | ")]

    def __repr__(self):
        return f"Rule(n={self.n}, options={self.options})"

    def _matches(self, message, rules):
        for option in self.options:
            yield from option._matches(message, rules)

    def is_valid(self, message, rules):
        return len(message) in self._matches(message, rules)


def parse_input(txt):
    rules, messages = txt.split("\n\n")
    rules = (Rule(rule_str) for rule_str in rules.splitlines())
    rules = {r.n: r for r in rules}
    return rules, messages


def parta(txt):
    rules, messages = parse_input(txt)
    return sum(rules[0].is_valid(m, rules) for m in messages.splitlines())


def partb(txt):
    rules, messages = parse_input(txt)
    rules[8] = Rule("8: 42 | 42 8")
    rules[11] = Rule("11: 42 31 | 42 11 31")
    return sum(rules[0].is_valid(m, rules) for m in messages.splitlines())


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
