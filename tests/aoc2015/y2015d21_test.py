import advent.aoc2015.day21 as d


def test_battle():
    player = d.Unit(8, 5, 5)
    boss = d.Unit(12, 7, 2)
    winner = d.battle(player, boss)
    assert winner is player
    assert boss.hit_points == 0
    assert player.hit_points == 2
