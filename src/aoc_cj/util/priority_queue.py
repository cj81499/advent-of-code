import dataclasses
from typing import Generic, TypeVar

from aoc_cj.util import Heap

T = TypeVar("T")


class PriorityQueue(Generic[T]):
    @dataclasses.dataclass(order=True)
    class PrioritizedItem:
        priority: int
        item: T = dataclasses.field(compare=False)

    def __init__(self):
        self.q = Heap()

    def __len__(self) -> int:
        return len(self.q)

    def push(self, priority: int, item: T):
        self.q.push(PriorityQueue.PrioritizedItem(priority, item))

    def pop(self) -> T:
        return self.q.pop().item
