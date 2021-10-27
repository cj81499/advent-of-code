from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def test_quine():
    quine = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    p = IntcodeProgram.parse(quine)
    p.run()
    assert ",".join(map(str, p.outputs)) == quine


def test_output_sixteen_digit_number():
    p = IntcodeProgram.parse("1102,34915192,34915192,7,4,7,99,0")
    p.run()
    assert len(p.outputs) == 1
    assert len(str(p.outputs[0])) == 16


def test_output_large_number():
    p = IntcodeProgram.parse("104,1125899906842624,99")
    p.run()
    assert len(p.outputs) == 1
    assert p.outputs[0] == 1125899906842624


def test_rel_base():
    p = IntcodeProgram.parse("109,19,204,-34")
    p[1985] = 1234567890
    p._relative_base = 2000
    p.run_next()
    assert p._relative_base == 2019
    p.run_next()
    assert len(p.outputs) == 1
    assert p.outputs[0] == 1234567890
