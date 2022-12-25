import pytest

import aoc_cj.aoc2022.day25 as d

EXAMPLE_INPUT = """
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
""".strip()


@pytest.mark.parametrize(
    ("example", "expected"),
    (
        l.strip().split()
        for l in """
1=-0-2     1747
 12111      906
  2=0=      198
    21       11
  2=01      201
   111       31
 20012     1257
   112       32
 1=-1=      353
  1-12      107
    12        7
    1=        3
   122       37
""".strip(
            "\n"
        ).splitlines()
    ),
)
def test_snafu_to_base_10(example: str, expected: str) -> None:
    assert d.snafu_to_base_10(example) == int(expected)


@pytest.mark.parametrize(
    ("example", "expected"),
    (
        l.strip().split()
        for l in """
        1              1
        2              2
        3             1=
        4             1-
        5             10
        6             11
        7             12
        8             2=
        9             2-
       10             20
       15            1=0
       20            1-0
     2022         1=11-2
    12345        1-0---0
314159265  1121-1110-1=0
""".strip(
            "\n"
        ).splitlines()
    ),
)
def test_base_10_to_snafu(example: str, expected: str) -> None:
    assert d.base_10_to_snafu(int(example)) == expected


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == "2=-1=0"
