import pytest

import aoc_cj.aoc2016.day04 as d

ROOM_1 = "aaaaa-bbb-z-y-x-123[abxyz]"
ROOM_2 = "a-b-c-d-e-f-g-h-987[abcde]"
ROOM_3 = "not-a-real-room-404[oarel]"
ROOM_4 = "totally-real-room-200[decoy]"

ROOMS = (ROOM_1, ROOM_2, ROOM_3, ROOM_4)


@pytest.mark.parametrize(
    "input, expected",
    [
        (ROOM_1, True),
        (ROOM_2, True),
        (ROOM_3, True),
        (ROOM_4, False),
    ],
)
def test_is_real_room(input: str, expected: bool) -> None:
    assert d.is_real_room(input) is expected


def test_part_1() -> None:
    assert d.part_1("\n".join(ROOMS)) == 1514


def test_decrypt() -> None:
    assert d.decrypt("qzmt-zixmtkozy-ivhz-343[ignore]") == "very encrypted name"
