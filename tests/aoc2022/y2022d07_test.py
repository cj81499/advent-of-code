import aoc_cj.aoc2022.day07 as d

EXAMPLE_INPUT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 95437


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 24933642
