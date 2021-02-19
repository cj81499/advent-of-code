import heapq
from typing import Generic, List, TypeVar

T = TypeVar('T')


class Heap(Generic[T]):
    def __init__(self, items: List[T] = []):
        self.heap = items.copy()
        heapq.heapify(self.heap)

    def __len__(self) -> int:
        return len(self.heap)

    def push(self, item: T):
        heapq.heappush(self.heap, item)

    def pop(self) -> T:
        return heapq.heappop(self.heap)

    def pushpop(self, item: T) -> T:
        return heapq.heappushpop(self.heap, item)

    def replace(self, item: T) -> T:
        return heapq.heapreplace(self.heap, item)

    @staticmethod
    def merge(*iterables, key=None, reverse=False):
        return heapq.merge(*iterables, key=key, reverse=reverse)

    @staticmethod
    def nlargest(n, iterable, key=None) -> List[T]:
        return heapq.nlargest(n, iterable, key=key)

    @staticmethod
    def nsmallest(n, iterable, key=None) -> List[T]:
        return heapq.nsmallest(n, iterable, key=key)
