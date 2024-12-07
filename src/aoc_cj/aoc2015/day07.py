import functools
from collections.abc import Mapping

from frozendict import frozendict


def signal_on(wire: str, wires: Mapping[str, str]) -> int:
    return _signal_on(wire, frozendict(wires))


@functools.cache
def _signal_on(wire: str, wires: Mapping[str, str]) -> int:
    if wire.isnumeric():
        return int(wire)
    val = wires[wire]
    if val.isnumeric():
        return int(val)
    if val.isalpha():
        return signal_on(val, wires)
    if val.startswith("NOT "):
        return ~signal_on(val.lstrip("NOT "), wires) & 0xFFFF
    lhs, op, rhs = val.split()
    if op == "LSHIFT":
        return signal_on(lhs, wires) << signal_on(rhs, wires)
    if op == "RSHIFT":
        return signal_on(lhs, wires) >> signal_on(rhs, wires)
    if op == "AND":
        return signal_on(lhs, wires) & signal_on(rhs, wires)
    if op == "OR":
        return signal_on(lhs, wires) | signal_on(rhs, wires)
    msg = f"unrecognized op: {op}"
    raise ValueError(msg)


def parse_wires(txt: str) -> dict[str, str]:
    wires = {}
    for line in txt.splitlines():
        l, r = line.split(" -> ")
        wires[r] = l
    return wires


def part_1(txt: str) -> int:
    wires = parse_wires(txt)
    return signal_on("a", wires)


def part_2(txt: str) -> int:
    wires = parse_wires(txt)
    wires["b"] = str(signal_on("a", wires))
    return signal_on("a", wires)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
