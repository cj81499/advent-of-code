from typing import Iterable, Tuple

from intcode_interpreter import run_intcode_program


def intcode_interpreter_test_helper(pairs: Iterable[Tuple[Iterable[int], Iterable[int]]]):  # noqa
    for memory, expected_output in pairs:
        assert run_intcode_program(memory) == expected_output
