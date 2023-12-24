import aoc_cj.aoc2023.day19 as d

EXAMPLE_INPUT = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
""".strip()


def test_parse_wf() -> None:
    wf = d.Workflow.parse("ex{x>10:one,m<20:two,a>30:R,A}")
    assert wf.name == "ex"
    assert wf.rules == [
        d.Rule("x", ">", 10, "one"),
        d.Rule("m", "<", 20, "two"),
        d.Rule("a", ">", 30, "R"),
    ]
    assert wf.fallback == "A"


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 19114


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 167409079868000
