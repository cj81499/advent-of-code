def part_1(txt: str) -> int:
    topo_map = [list(map(int, line)) for line in txt.splitlines()]
    trailheads = [(x, y) for y, row in enumerate(topo_map) for x, c in enumerate(row) if c == 0]
    score_sum = 0
    for trailhead in trailheads:
        reachable_summits = set[tuple[int, int]]()
        to_explore = set[tuple[tuple[int, int], int]]()
        to_explore.add((trailhead, 0))
        while to_explore:
            (x, y), height = to_explore.pop()
            assert topo_map[y][x] == height
            assert 0 <= height <= 9
            needed_height = height + 1
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_y < len(topo_map) and 0 <= new_x < len(topo_map[new_y]):
                    val = topo_map[new_y][new_x]
                    if val == needed_height:
                        if val == 9:
                            reachable_summits.add((new_x, new_y))
                        else:
                            to_explore.add(((new_x, new_y), needed_height))
        score = len(reachable_summits)
        score_sum += score
    return score_sum


def part_2(txt: str) -> int:
    topo_map = [list(map(int, line)) for line in txt.splitlines()]
    trailheads = [(x, y) for y, row in enumerate(topo_map) for x, c in enumerate(row) if c == 0]
    score_sum = 0
    for trailhead in trailheads:
        to_explore = list[tuple[tuple[int, int], int]]()
        to_explore.append((trailhead, 0))
        while to_explore:
            (x, y), height = to_explore.pop()
            assert topo_map[y][x] == height
            assert 0 <= height <= 9
            needed_height = height + 1
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_y < len(topo_map) and 0 <= new_x < len(topo_map[new_y]):
                    val = topo_map[new_y][new_x]
                    if val == needed_height:
                        if val == 9:
                            score_sum += 1
                        else:
                            to_explore.append(((new_x, new_y), needed_height))
    return score_sum


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
