import dataclasses
import re
from typing import Optional

PATTERN = re.compile(r" ([A-Z]) ")


class StepManager:
    _unstarted_requirements: dict[str, set[str]]
    _in_progress: set[str]
    _finished: set[str]

    def __init__(self) -> None:
        self._unstarted_requirements = {}
        self._in_progress = set()
        self._finished = set()

    def __bool__(self) -> bool:
        return not self._finished_steps()

    def next_step(self) -> Optional[str]:
        return min((k for k, blocked_by in self._unstarted_requirements.items() if len(blocked_by) == 0), default=None)

    def start(self, step: str) -> None:
        self._unstarted_requirements.pop(step)
        self._in_progress.add(step)

    def finish(self, step: str) -> None:
        self._unstarted_requirements.pop(step, None)
        self._in_progress.discard(step)
        self._finished.add(step)
        for blockers in self._unstarted_requirements.values():
            blockers.discard(step)

    def _require(self, step: str, requirement: str) -> None:
        self._unstarted_requirements.setdefault(step, set()).add(requirement)
        self._unstarted_requirements.setdefault(requirement, set())

    def _finished_steps(self):
        return len(self._unstarted_requirements) == 0 and len(self._in_progress) == 0

    @staticmethod
    def parse(txt: str):
        r = StepManager()
        for line in txt.splitlines():
            requirement, step = PATTERN.findall(line)
            r._require(step, requirement)
        return r


def parta(txt: str):
    steps = StepManager.parse(txt)

    order = []
    while steps:
        selected_step = steps.next_step()
        order.append(selected_step)
        steps.finish(selected_step)

    return "".join(order)


def partb(txt: str, num_workers: int = 5, base_duration: int = 60):
    @dataclasses.dataclass
    class Worker:
        working_on: Optional[str] = None
        remaining_time: int = 0

    workers = [Worker() for _ in range(num_workers)]

    steps = StepManager.parse(txt)

    duration = 0
    while steps:
        available_workers = (w for w in workers if w.working_on is None)
        for w in available_workers:
            if selected_step := steps.next_step():
                steps.start(selected_step)
                w.working_on = selected_step
                w.remaining_time = ord(selected_step) - ord("A") + 1 + base_duration

        assigned_workers = (w for w in workers if w.working_on is not None)
        for w in assigned_workers:
            w.remaining_time -= 1
            if w.remaining_time == 0:
                steps.finish(w.working_on)
                w.working_on = None

        duration += 1

    return duration


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
