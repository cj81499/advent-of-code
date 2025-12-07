import pytest

import aoc_cj.aoc2018.day20 as d

EXAMPLE_INPUT_0 = "^WNE$"
EXAMPLE_INPUT_1 = "^ENWWW(NEEE|SSE(EE|N))$"
EXAMPLE_INPUT_2 = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
EXAMPLE_INPUT_3 = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
EXAMPLE_INPUT_4 = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        (EXAMPLE_INPUT_0, 3),
        (EXAMPLE_INPUT_1, 10),
        (EXAMPLE_INPUT_2, 18),
        (EXAMPLE_INPUT_3, 23),
        (EXAMPLE_INPUT_4, 31),
    ],
)
def test_part_1(example: str, expected) -> None:
    assert d.part_1(example) == expected
