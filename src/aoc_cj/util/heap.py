import heapq
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Heap(Generic[T]):
    def __init__(self, items: Optional[list[T]] = None):
        self._heap = [] if items is None else items.copy()
        heapq.heapify(self._heap)

    def __len__(self) -> int:
        return len(self._heap)

    def push(self, item: T) -> None:
        heapq.heappush(self._heap, item)

    def pop(self) -> T:
        return heapq.heappop(self._heap)

    def pushpop(self, item: T) -> T:
        return heapq.heappushpop(self._heap, item)

    def replace(self, item: T) -> T:
        return heapq.heapreplace(self._heap, item)
