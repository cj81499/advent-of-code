import dataclasses
import itertools
import re

import z3  # type: ignore[import-untyped]

from aoc_cj import util

_PARSER = re.compile(r"\[(.*)\] (.*) \{(.*)\}")


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Machine:
    indicator_lights: tuple[bool, ...]
    buttons: tuple[tuple[int, ...], ...]
    joltage_reqs: tuple[int, ...]

    @staticmethod
    def parse(txt: str) -> "Machine":
        match = _PARSER.fullmatch(txt)
        assert match is not None
        indicator_lights, button_wiring_schematics, joltage_reqs = match.groups()
        return Machine(
            indicator_lights=tuple(light == "#" for light in indicator_lights),
            buttons=tuple(tuple(util.ints(s)) for s in button_wiring_schematics.split(" ")),
            joltage_reqs=tuple(util.ints(joltage_reqs)),
        )

    def minimum_presses_lights(self) -> int:
        for press_count in itertools.count(1):
            for presses in itertools.combinations(self.buttons, r=press_count):
                lights = [False] * len(self.indicator_lights)
                for button in presses:
                    for i in button:
                        lights[i] = not lights[i]
                if tuple(lights) == self.indicator_lights:
                    return press_count
        assert False, "unreachable"

    def minimum_presses_joltage(self) -> int:
        opt = z3.Optimize()

        total_presses = z3.Int("total presses")
        button_press_counts = {b: z3.Int(f"btn {b} presses") for b in self.buttons}

        # each button must be pressed a nonnegative number of times
        for btn_press_count in button_press_counts.values():
            opt.add(btn_press_count >= 0)

        # for each joltage req, find the buttons that "influence" (increment) it
        # when they're pressed. require the sum of the number of times those
        # buttons are pressed to be equal the joltage req
        for i, req in enumerate(self.joltage_reqs):
            influenced_by = (button_press_counts[btn] for btn in self.buttons if i in btn)
            opt.add(req == sum(influenced_by))

        opt.add(total_presses == sum(button_press_counts.values()))
        opt.minimize(total_presses)

        assert opt.check() == z3.sat
        model = opt.model()
        return int(model[total_presses].as_long())


def part_1(txt: str) -> int:
    machines = map(Machine.parse, txt.splitlines())
    return sum(m.minimum_presses_lights() for m in machines)


def part_2(txt: str) -> int:
    machines = map(Machine.parse, txt.splitlines())
    return sum(m.minimum_presses_joltage() for m in machines)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
