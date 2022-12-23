import dataclasses
import heapq
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclasses.dataclass(order=True)
class PrioritizedItem(Generic[T]):
    priority: int
    item: T = dataclasses.field(compare=False)


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._repr: list[PrioritizedItem[T]] = []

    def __len__(self) -> int:
        return len(self._repr)

    def push(self, priority: int, item: T) -> None:
        heapq.heappush(self._repr, PrioritizedItem(priority, item))

    def pop(self) -> T:
        return heapq.heappop(self._repr).item
