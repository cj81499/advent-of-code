import itertools
import operator

import pytest

from advent.aoc2019.intcode_computer import IntcodeProgram


def helper(program, input, expected):
    p = IntcodeProgram.parse(program)
    p.write_input(input)
    p.run()
    assert len(p.outputs) == 1 and p.outputs[0] == expected


@pytest.mark.parametrize("n", range(10))
def test_input_output(n):
    helper("3,0,4,0,99", n, n)


def test_parameter_modes():
    p = IntcodeProgram.parse("1002,4,3,4,33")
    p.run()
    assert ",".join(map(str, p.state)) == "1002,4,3,4,99"


def test_negative_int():
    p = IntcodeProgram.parse("1101,100,-1,4,0")
    p.run()
    assert p[4] == 99


@pytest.mark.parametrize("n, program_op_pair", itertools.product(
    range(10), (
        ("3,9,8,9,10,9,4,9,99,-1,8", operator.eq),  # position mode, equal to
        ("3,9,7,9,10,9,4,9,99,-1,8", operator.lt),  # position mode, less than
        ("3,3,1108,-1,8,3,4,3,99", operator.eq),  # position mode, equal to
        ("3,3,1107,-1,8,3,4,3,99", operator.lt),  # position mode, less than
    ),
))
def test_compare_eight(n, program_op_pair):
    program, op = program_op_pair
    helper(program, n, 1 if op(n, 8) else 0)


@pytest.mark.parametrize("n, program", itertools.product(
    range(10), (
        ("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"),  # position mode
        ("3,3,1105,-1,9,1101,0,0,12,4,12,99,1"),  # immediate mode
    ),
))
def test_jumps(n, program):
    helper(program, n, 0 if n == 0 else 1)


LARGER_EXAMPLE = """
3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
""".strip().replace("\n", "")


@pytest.mark.parametrize("n", range(10))
def test_larger_example(n):
    helper(LARGER_EXAMPLE, n, 999 if n < 8 else (1000 if n == 8 else 1001))
