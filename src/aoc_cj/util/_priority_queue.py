import dataclasses
import heapq
from typing import Generic, TypeVar

__all__ = ("PriorityQueue",)


T = TypeVar("T")


@dataclasses.dataclass(order=True)
class _PrioritizedItem(Generic[T]):
    priority: int
    item: T = dataclasses.field(compare=False)


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._repr: list[_PrioritizedItem[T]] = []

    def __len__(self) -> int:
        return len(self._repr)

    def push(self, priority: int, item: T) -> None:
        heapq.heappush(self._repr, _PrioritizedItem(priority, item))

    def pop(self) -> T:
        return heapq.heappop(self._repr).item
