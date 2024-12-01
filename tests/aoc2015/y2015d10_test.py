import aoc_cj.aoc2015.day10 as d


def test_day10() -> None:
    assert d.look_and_say("1", rounds=1) == "11"
    assert d.look_and_say("1", rounds=2) == "21"
    assert d.look_and_say("1", rounds=3) == "1211"
    assert d.look_and_say("1", rounds=4) == "111221"
    assert d.look_and_say("1", rounds=5) == "312211"
    assert d.look_and_say("1", rounds=6) == "13112221"
    assert d.look_and_say("1", rounds=7) == "1113213211"
    assert d.look_and_say("1", rounds=8) == "31131211131221"
    assert d.look_and_say("1", rounds=9) == "13211311123113112211"
    assert d.look_and_say("1", rounds=10) == "11131221133112132113212221"
