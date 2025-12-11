import pytest

import aoc_cj.aoc2021.day16 as d


def test_parse_packet_1() -> None:
    packet = d.parse_packet(d.hex_to_binary("38006F45291200"))
    assert isinstance(packet, d.OperatorPacket)
    assert packet.version == 1
    assert packet.type_id == 6
    assert len(packet.children) == 2
    first_child, second_child = packet.children
    assert isinstance(first_child, d.LiteralValuePacket)
    assert first_child.value == 10
    assert isinstance(second_child, d.LiteralValuePacket)
    assert second_child.value == 20


@pytest.mark.parametrize(
    ("packet", "version_sum"),
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_part_1(packet, version_sum) -> None:
    assert d.part_1(packet) == version_sum


@pytest.mark.parametrize(
    ("packet", "result"),
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_part_2(packet, result) -> None:
    assert d.part_2(packet) == result
