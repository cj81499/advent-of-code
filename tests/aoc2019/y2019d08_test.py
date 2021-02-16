import advent.aoc2019.day08 as d


def test_parta() -> None:
    nums = [int(x) for x in "123456789012"]
    assert d.get_layers(nums, 3, 2) == [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 0, 1, 2]
    ]


def test_partb() -> None:
    nums = [int(x) for x in "0222112222120000"]
    layers = d.get_layers(nums, 2, 2)
    assert layers == [
        [0, 2, 2, 2],
        [1, 1, 2, 2],
        [2, 2, 1, 2],
        [0, 0, 0, 0]
    ]
    assert d.render(layers, 2) == " #\n# "
