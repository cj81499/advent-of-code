import aoc_cj.aoc2019.day17 as d

EXAMPLE_INPUT_0 = """
..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..
""".strip()


EXAMPLE_INPUT_1 = """
#######...#####
#.....#...#...#
#.....#...#...#
......#...#...#
......#...###.#
......#.....#.#
^########...#.#
......#.#...#.#
......#########
........#...#..
....#########..
....#...#......
....#...#......
....#...#......
....#####......
""".strip()

FULL_ROUTE = "R,8,R,8,R,4,R,4,R,8,L,6,L,2,R,4,R,4,R,8,R,8,R,8,L,6,L,2"


def test_sum_of_alignment_parameters():
    assert d.sum_of_alignment_parameters(EXAMPLE_INPUT_0) == 76


def test_full_route():
    assert d.full_route(EXAMPLE_INPUT_1) == FULL_ROUTE


def test_plan_route():
    # at most 20 characters
    plan = d.plan_route(FULL_ROUTE)
    assert all(len(p) <= 20 for p in plan)
    (
        main,
        a,
        b,
        c,
    ) = plan
    print(main)
    fns = {"A": a, "B": b, "C": c}
    main = [fns[x] for x in main]
    main = [x for subl in main for x in subl]
    assert ",".join(main) == FULL_ROUTE
