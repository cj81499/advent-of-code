import dataclasses
from typing import Generic, TypeVar

from aoc_cj.util.heap import Heap

T = TypeVar("T")


@dataclasses.dataclass(order=True)
class PrioritizedItem(Generic[T]):
    priority: int
    item: T = dataclasses.field(compare=False)


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._pq: Heap[PrioritizedItem[T]] = Heap()

    def __len__(self) -> int:
        return len(self._pq)

    def push(self, priority: int, item: T) -> None:
        self._pq.push(PrioritizedItem(priority, item))

    def pop(self) -> T:
        return self._pq.pop().item
