from typing import Iterable

from intcode_interpreter import run_intcode_program


def run_intcode_test(memory: Iterable[int], expected_output: Iterable[int]):
    assert run_intcode_program(memory) == expected_output
