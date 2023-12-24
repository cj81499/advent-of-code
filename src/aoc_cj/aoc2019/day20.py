import heapq
from collections import deque
from functools import total_ordering


def part_1(txt: str):
    grid, portals, start, end = parse(txt)

    q = deque([(0, start)])
    seen = set()
    shortest_dist = float("inf")
    while q:
        steps, pos = q.popleft()
        if pos not in seen:
            if pos == end:
                shortest_dist = min(shortest_dist, steps)
            if grid.get(pos) == ".":
                if pos in portals:
                    q.append((steps + 1, portals[pos]))
                q.extend((steps + 1, pos + delta) for delta in (-1j, 1, 1j, -1))
            seen.add(pos)
    return shortest_dist


@total_ordering
class ComparableComplex(complex):
    def __lt__(self, other):
        if self.imag != other.imag:
            return self.imag < other.imag
        if self.real != other.real:
            return self.real < other.real
        return 0

    def __add__(self, other):
        return ComparableComplex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComparableComplex(self.real - other.real, self.imag - other.imag)


def part_2(txt: str):
    grid, portals, start, end = parse(txt)

    inner_portals = get_inner_portals(grid, portals)

    q = []
    heapq.heappush(q, (0, 0, start))
    seen = set()
    shortest_dist = float("inf")
    while q:
        steps, layer, pos = heapq.heappop(q)
        if steps > shortest_dist:
            break
        if (pos, layer) not in seen:
            if pos == end and layer == 0:
                shortest_dist = min(shortest_dist, steps)
            if grid.get(pos) == ".":
                if pos in portals:
                    if pos in inner_portals:
                        heapq.heappush(q, (steps + 1, layer + 1, portals[pos]))
                    elif layer >= 1:
                        heapq.heappush(q, (steps + 1, layer - 1, portals[pos]))
                for node in ((steps + 1, layer, pos + delta) for delta in (-1j, 1, 1j, -1)):
                    heapq.heappush(q, node)
            seen.add((pos, layer))
    return shortest_dist


def get_inner_portals(grid, portals):
    max_x = int(max(p.real for p in grid))
    max_y = int(max(p.imag for p in grid))

    def is_inner(pos):
        r, i = pos.real, pos.imag
        return not (r == 2 or i == 2 or r == max_x - 2 or i == max_y - 2)

    return {p for p in portals if is_inner(p)}


def parse(txt):
    grid = {}
    portals = {}
    for y, row in enumerate(txt.splitlines()):
        for x, c in enumerate(row):
            p = ComparableComplex(x, y)
            if c != " ":
                grid[p] = c
            if c.isalpha():
                up = p - 1j
                up_val = grid.get(up, "")
                left = p - 1
                left_val = grid.get(left, "")
                if up_val.isalpha():
                    portals.setdefault(up_val + c, []).append(p - 2j if grid.get(p - 2j) == "." else p + 1j)
                elif left_val.isalpha():
                    portals.setdefault(left_val + c, []).append(p - 2 if grid.get(p - 2) == "." else p + 1)
    assert all(len(pos) == (1 if name == "AA" or name == "ZZ" else 2) for name, pos in portals.items())
    start = portals.pop("AA")[0]
    end = portals.pop("ZZ")[0]
    new_portals = {}
    for a, b in portals.values():
        new_portals[a] = b
        new_portals[b] = a
    portals = new_portals
    return grid, portals, start, end


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
