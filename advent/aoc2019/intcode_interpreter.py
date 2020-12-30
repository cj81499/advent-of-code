from collections import deque
from typing import Callable

EXIT_OPCODE = 99

POSITION_MODE = 0
IMMEDIATE_MODE = 1

inputs = None


def get_param(n, memory, ip, mode):
    val = memory[ip + n]
    if mode == IMMEDIATE_MODE:
        return val
    return memory[val]


def _arithmetic_opcode_helper(memory, ip, modes, operation: Callable):  # noqa
    """
    Dunder methods to be used as operation for future arithmetic opcodes:
    https://www.python-course.eu/python3_magic_methods.php
    """

    p_1 = get_param(1, memory, ip, modes[0])
    p_2 = get_param(2, memory, ip, modes[1])

    # ? this donesn't make sense b/c paramaters that are written to are never
    # in immediate_mode
    p_3 = get_param(3, memory, ip, IMMEDIATE_MODE)

    memory = [x for x in memory]
    memory[p_3] = operation(p_1, p_2)

    return tuple(memory)


def _handle_opcode_1(memory, ip, modes):
    return _arithmetic_opcode_helper(memory, ip, modes, int.__add__)


def _handle_opcode_2(memory, ip, modes):
    return _arithmetic_opcode_helper(memory, ip, modes, int.__mul__)


def _handle_opcode_3(memory, ip, modes):
    global inputs
    val = inputs.popleft()
    p_1 = get_param(1, memory, ip, IMMEDIATE_MODE)
    return [val if i == p_1 else x for i, x in enumerate(memory)]


def _handle_opcode_4(memory, ip, modes):
    p_1 = get_param(1, memory, ip, modes[0])
    print(p_1)
    return memory


# def _handle_opcode_5(memory, ip, modes):
#     p_1 = get_param(1, memory, ip, modes[0])
#     return memory
def run_intcode_program(memory, prog_inputs=None):
    global inputs
    inputs = deque(prog_inputs) if prog_inputs else deque()
    # handler, param_count
    OPCODE_INFO: dict[int, Callable] = {
        1: (_handle_opcode_1, 3),
        2: (_handle_opcode_2, 3),
        3: (_handle_opcode_3, 1),
        4: (_handle_opcode_4, 1),
        # 5: (_handle_opcode_5, 2),
        # 6: (_handle_opcode_6, 2),
        # 7: (_handle_opcode_7, 3),
        # 8: (_handle_opcode_8, 3),
    }

    ip = 0
    while True:
        instruction = str(memory[ip])
        opcode = int(instruction[-2:])
        param_1_mode = int(instruction[-3:-2] or 0)
        param_2_mode = int(instruction[-4:-3] or 0)
        param_3_mode = int(instruction[-5:-4] or 0)
        modes = (param_1_mode, param_2_mode, param_3_mode)
        # print(opcode, modes)
        # exit()

        if opcode == EXIT_OPCODE:
            return memory

        # print(instruction, opcode)
        handler, param_count = OPCODE_INFO.get(opcode)
        if handler:
            memory = handler(memory, ip, modes)
            ip += param_count + 1  # plus 1 for instruction
        else:
            raise AssertionError(f"Invalid opcode: {opcode}.")
