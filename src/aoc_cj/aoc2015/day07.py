from functools import cache
from operator import and_, lshift, or_, rshift


class HashableDict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))


@cache
def signal_on(wire, wires):
    if wire.isnumeric():
        return int(wire)
    val = wires[wire]
    if val.isnumeric():
        return int(val)
    if val.isalpha():
        return signal_on(val, wires)
    if "NOT" in val:
        return ~signal_on(val.lstrip("NOT "), wires) & 0xFFFF
    lhs, op, rhs = val.split()
    return {
        "LSHIFT": lshift,
        "RSHIFT": rshift,
        "AND": and_,
        "OR": or_,
    }[op](signal_on(lhs, wires), signal_on(rhs, wires))


def parse_wires(txt):
    return dict(reversed(line.split(" -> ")) for line in txt.splitlines())


def part_1(txt: str):
    wires = HashableDict(parse_wires(txt))
    return signal_on("a", wires)


def part_2(txt: str):
    wires = HashableDict(parse_wires(txt))
    wires["b"] = str(signal_on("a", wires))
    return signal_on("a", wires)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
