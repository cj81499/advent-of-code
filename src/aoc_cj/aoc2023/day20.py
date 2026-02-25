import abc
import dataclasses
import enum
import itertools
import math
import re
from collections import Counter, deque
from collections.abc import Callable, Sequence
from typing import NewType, override

ModuleName = NewType("ModuleName", str)
SendPulse = Callable[["Pulse"], None]


class PulseKind(enum.Enum):
    LOW = enum.auto()
    HIGH = enum.auto()


@dataclasses.dataclass(frozen=True)
class Pulse:
    kind: PulseKind
    source: ModuleName
    destination: ModuleName


@dataclasses.dataclass
class Module(abc.ABC):
    name: ModuleName
    destination_modules: Sequence[ModuleName]
    send_pulse: SendPulse

    @abc.abstractmethod
    def receive_pulse(self, pulse: Pulse) -> None: ...

    def emit_pulse_kind(self, pulse_kind: PulseKind) -> None:
        for destination in self.destination_modules:
            self.send_pulse(Pulse(pulse_kind, self.name, destination))


@dataclasses.dataclass
class FlipFlopModule(Module):
    on: bool = False

    @override
    def receive_pulse(self, pulse: Pulse) -> None:
        if pulse.kind == PulseKind.LOW:
            send_pulse_kind = PulseKind.LOW if self.on else PulseKind.HIGH
            self.on = not self.on
            self.emit_pulse_kind(send_pulse_kind)


@dataclasses.dataclass
class ConjunctionModule(Module):
    memory: dict[ModuleName, PulseKind] = dataclasses.field(default_factory=dict)

    @override
    def receive_pulse(self, pulse: Pulse) -> None:
        self.memory[pulse.source] = pulse.kind
        self.emit_pulse_kind(
            PulseKind.LOW if all(v == PulseKind.HIGH for v in self.memory.values()) else PulseKind.HIGH
        )


class BroadcastModule(Module):
    @override
    def receive_pulse(self, pulse: Pulse) -> None:
        self.emit_pulse_kind(pulse.kind)


_MODULE_PATTERN = re.compile(r"(?P<kind>[%&])?(?P<name>[a-z]+) -> (?P<destination_modules>([a-z]+, )*[a-z]+)")


def parse_module(s: str, send_pulse: SendPulse) -> Module:
    match = _MODULE_PATTERN.match(s)
    assert match is not None, f"match None for '{s}'"

    name = match.group("name")
    destination_modules = [ModuleName(n) for n in match.group("destination_modules").split(", ")]
    kind = match.group("kind")
    module_cls: type[Module]
    if kind is None:
        assert name == "broadcaster"
        module_cls = BroadcastModule
    elif kind == "%":
        module_cls = FlipFlopModule
    elif kind == "&":
        module_cls = ConjunctionModule
    else:
        assert False, "unreachable"
    return module_cls(ModuleName(name), destination_modules, send_pulse)


def part_1(txt: str) -> int:
    pulses: deque[Pulse] = deque()
    modules = {(m := parse_module(line, pulses.append)).name: m for line in txt.splitlines()}

    # inform each conjunction node of its sources
    conjunction_modules = {mod_name: mod for mod_name, mod in modules.items() if isinstance(mod, ConjunctionModule)}
    for module_name, module in modules.items():
        for destination_module_name in module.destination_modules:
            if (conjunction_module := conjunction_modules.get(destination_module_name, None)) is not None:
                conjunction_module.memory[module_name] = PulseKind.LOW

    pulse_counts: Counter[PulseKind] = Counter()
    for _ in range(1000):
        # push button
        pulses.append(Pulse(PulseKind.LOW, ModuleName("button"), ModuleName("broadcaster")))

        # handle pulses
        while pulses:
            pulse = pulses.popleft()
            pulse_counts[pulse.kind] += 1
            if (mod := modules.get(pulse.destination)) is not None:
                mod.receive_pulse(pulse)

    return math.prod(pulse_counts.values())


def part_2(txt: str) -> int:  # pragma: no cover
    raise NotImplementedError()
    pulses: deque[Pulse] = deque()  # type: ignore[unreachable]
    modules = {(m := parse_module(line, pulses.append)).name: m for line in txt.splitlines()}

    # inform each conjunction node of its sources
    conjunction_modules = {mod_name: mod for mod_name, mod in modules.items() if isinstance(mod, ConjunctionModule)}
    for module_name, module in modules.items():
        for destination_module_name in module.destination_modules:
            if (conjunction_module := conjunction_modules.get(destination_module_name, None)) is not None:
                conjunction_module.memory[module_name] = PulseKind.LOW

    for button_presses in itertools.count(1):
        if button_presses % 100000 == 0:
            print(button_presses)
        # push button
        pulses.append(Pulse(PulseKind.LOW, ModuleName("button"), ModuleName("broadcaster")))

        # handle pulses
        while pulses:
            pulse = pulses.popleft()
            if pulse.destination == "rx" and pulse.kind == PulseKind.LOW:
                return button_presses
            if (mod := modules.get(pulse.destination)) is not None:
                mod.receive_pulse(pulse)
    assert False, "unreachable"


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
