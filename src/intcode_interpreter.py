from typing import Callable, Dict, List

EXIT_OPCODE = 99


def _arithmetic_opcode_helper(memory: List[int], ip: int, operation: Callable) -> List[int]:  # noqa
    """
    Dunder methods to be used as operation for future arithmetic opcodes:
    https://www.python-course.eu/python3_magic_methods.php
    """

    pos_1 = memory[ip + 1]
    pos_2 = memory[ip + 2]
    pos_3 = memory[ip + 3]

    val_1 = memory[pos_1]
    val_2 = memory[pos_2]

    # work with a copy of memory to avoid side effects
    memory = [x for x in memory]
    memory[pos_3] = operation(val_1, val_2)

    return memory


def _handle_opcode_1(memory: List[int], ip: int) -> List[int]:
    return _arithmetic_opcode_helper(memory, ip, int.__add__)


def _handle_opcode_2(memory: List[int], ip: int) -> List[int]:
    return _arithmetic_opcode_helper(memory, ip, int.__mul__)


def run_intcode_program(memory: List[int]) -> List[int]:
    # handler, instruction_size
    OPCODE_INFO: Dict[int, Callable] = {
        1: (_handle_opcode_1, 4),
        2: (_handle_opcode_2, 4)
    }

    ip = 0
    while True:
        opcode = memory[ip]

        if opcode == EXIT_OPCODE:
            return memory

        handler, instruction_size = OPCODE_INFO.get(opcode)
        if handler:
            memory = handler(memory, ip)
            ip += instruction_size
        else:
            raise AssertionError(f"Invalid opcode: {opcode}.")
