import dataclasses
import heapq

__all__ = ("PriorityQueue",)


@dataclasses.dataclass(order=True)
class _PrioritizedItem[T]:
    priority: int
    item: T = dataclasses.field(compare=False)


class PriorityQueue[T]:
    def __init__(self) -> None:
        self._repr: list[_PrioritizedItem[T]] = []

    def __len__(self) -> int:
        return len(self._repr)

    def push(self, priority: int, item: T) -> None:
        heapq.heappush(self._repr, _PrioritizedItem(priority, item))

    def pop(self) -> T:
        return self.pop_with_priority()[0]

    def pop_with_priority(self) -> tuple[T, int]:
        res = heapq.heappop(self._repr)
        return res.item, res.priority
