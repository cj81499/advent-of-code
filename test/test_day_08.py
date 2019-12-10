import path_fix
import day_08


def test_day_08_part1_0():
    nums = [int(x) for x in "123456789012"]
    assert day_08.get_layers(nums, 3, 2) == [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 0, 1, 2]
    ]


def test_day_08_part2_0():
    nums = [int(x) for x in "0222112222120000"]
    layers = day_08.get_layers(nums, 2, 2)
    assert layers == [
        [0, 2, 2, 2],
        [1, 1, 2, 2],
        [2, 2, 1, 2],
        [0, 0, 0, 0]
    ]
    assert day_08.render(layers, 2) == " X\nX "
