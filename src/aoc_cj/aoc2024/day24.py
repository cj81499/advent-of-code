import dataclasses
import enum
import re
from typing import ClassVar, Self, assert_never


class Op(enum.StrEnum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"

    def apply(self, a: bool, b: bool) -> bool:
        if self is Op.AND:
            return a and b
        if self is Op.OR:
            return a or b
        if self is Op.XOR:
            return a ^ b
        assert_never(self)


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Gate:
    left: str
    op: Op
    right: str
    out: str

    _PATTERN: ClassVar = re.compile(r"^(.+) (AND|OR|XOR) (.+) -> (.+)$")

    @classmethod
    def parse(cls, txt: str) -> Self:
        match = cls._PATTERN.fullmatch(txt)
        if match is None:
            msg = f"Failed to parse {txt} as a {cls.__name__}."
            raise ValueError(msg)
        l, op, r, out = match.groups()
        return cls(left=l, op=Op(op), right=r, out=out)


def part_1(txt: str) -> int:
    gates, wires = _parse(txt)

    unhandled_gates = gates
    while unhandled_gates:
        handled = set[Gate]()
        for gate in unhandled_gates:
            if (l := wires.get(gate.left)) is not None and (r := wires.get(gate.right)) is not None:
                wires[gate.out] = gate.op.apply(l, r)
                handled.add(gate)
        assert len(handled) != 0, "Failed to handle any gates"
        unhandled_gates = unhandled_gates.difference(handled)

    z_wires = {k: v for k, v in wires.items() if k.startswith("z")}
    return sum((2**i if v else 0) for i, (k, v) in enumerate(sorted(z_wires.items())))


def part_2(txt: str) -> int:
    raise NotImplementedError()


def _parse(txt: str) -> tuple[frozenset[Gate], dict[str, bool]]:
    initial_values, gates = txt.split("\n\n")
    wires: dict[str, bool] = {}
    for line in initial_values.splitlines():
        name, sep, value = line.partition(": ")
        assert sep == ": ", line
        wires[name] = bool(int(value))
    gates = frozenset(map(Gate.parse, gates.splitlines()))
    return gates, wires


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
