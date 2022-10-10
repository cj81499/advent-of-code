import abc
import dataclasses
from collections.abc import Iterable, Sequence
from math import prod
from typing import Literal, cast

from more_itertools import ichunked, take
from more_itertools.more import peekable

Binary = Literal[0, 1]


@dataclasses.dataclass
class Packet(abc.ABC):
    version: int
    type_id: int

    def version_sum(self) -> int:
        return self.version

    def evaluate(self) -> int:
        pass


@dataclasses.dataclass
class LiteralValuePacket(Packet):
    value: int

    def __post_init__(self) -> None:
        assert self.type_id == 4

    def evaluate(self) -> int:
        return self.value


@dataclasses.dataclass
class OperatorPacket(Packet):
    children: Sequence[Packet]

    def version_sum(self) -> int:
        return super().version_sum() + sum(c.version_sum() for c in self.children)

    def evaluate(self) -> int:
        # Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
        if self.type_id == 0:
            return sum(c.evaluate() for c in self.children)
        # Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
        if self.type_id == 1:
            return prod(c.evaluate() for c in self.children)
        # Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
        if self.type_id == 2:
            return min(c.evaluate() for c in self.children)
        # Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
        if self.type_id == 3:
            return max(c.evaluate() for c in self.children)
        # Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
        if self.type_id == 5:
            assert len(self.children) == 2
            a, b = self.children
            return 1 if a.evaluate() > b.evaluate() else 0
        # Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
        if self.type_id == 6:
            assert len(self.children) == 2
            a, b = self.children
            return 1 if a.evaluate() < b.evaluate() else 0
        # Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
        if self.type_id == 7:
            assert len(self.children) == 2
            a, b = self.children
            return 1 if a.evaluate() == b.evaluate() else 0
        assert False, "unreachable"

    def __post_init__(self) -> None:
        assert self.type_id != 4


def binary_to_int(binary: Iterable[Binary]) -> int:
    n = 0
    for bit in binary:
        n <<= 1
        n |= bit
    return n


def parse_packet(binary: Iterable[Binary]) -> Packet:
    version = binary_to_int(take(3, binary))
    type_id = binary_to_int(take(3, binary))

    if type_id == 4:  # literal value
        value = 0
        for c in ichunked(binary, 5):
            first = next(c)
            for b in c:
                value <<= 1
                value |= b
            if first == 0:
                break
        return LiteralValuePacket(version, type_id, value)

    # operator packet
    length_type_id = next(binary)

    children = []
    if length_type_id == 0:
        # next 15 bits are a number that represents the
        # total length in bits of the sub-packets contained by this packet
        total_length_in_bits = binary_to_int(take(15, binary))
        bits = peekable(take(total_length_in_bits, binary))
        while bits:
            children.append(parse_packet(bits))
    else:
        # next 11 bits are a number that represents the
        # number of sub-packets immediately contained by this packet
        number_of_sub_packets = binary_to_int(take(11, binary))
        for _ in range(number_of_sub_packets):
            children.append(parse_packet(binary))

    return OperatorPacket(version, type_id, children)


def hex_to_binary(hex: str) -> Iterable[Binary]:
    for nibble in (int(c, 16) for c in hex):  # a nibble is 4 bits
        # TODO: clean up
        for _ in range(4):
            bit = (nibble & 0b1000) >> 3
            assert bit in {0, 1}
            yield cast(Binary, bit)
            nibble <<= 1


def parta(txt: str) -> int:
    packet = parse_packet(hex_to_binary(txt))
    return packet.version_sum()


def partb(txt: str) -> int:
    packet = parse_packet(hex_to_binary(txt))
    return packet.evaluate()


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
