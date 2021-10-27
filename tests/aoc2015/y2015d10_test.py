import aoc_cj.aoc2015.day10 as d


def test_day10():
    assert d.look_and_say("1", 1) == "11"
    assert d.look_and_say("1", 2) == "21"
    assert d.look_and_say("1", 3) == "1211"
    assert d.look_and_say("1", 4) == "111221"
    assert d.look_and_say("1", 5) == "312211"
    assert d.look_and_say("1", 6) == "13112221"
    assert d.look_and_say("1", 7) == "1113213211"
    assert d.look_and_say("1", 8) == "31131211131221"
    assert d.look_and_say("1", 9) == "13211311123113112211"
    assert d.look_and_say("1", 10) == "11131221133112132113212221"
