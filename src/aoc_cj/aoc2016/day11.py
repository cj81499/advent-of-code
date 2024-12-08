import itertools
from collections import deque
from collections.abc import Generator, Sequence

NUM_FLOORS = 4
ITEM_TYPES = ("generator", "microchip")
NEW_ELEMENTS = ("elerium", "dilithium")


def part_1(txt: str) -> int:
    return helper(txt)


def part_2(txt: str) -> int:
    return helper(txt, extra_items=True)


def helper(txt: str, *, extra_items: bool = False) -> int:
    q = deque([(0, (0, parse(txt, extra_items=extra_items)))])
    seen = set()
    while len(q) > 0:
        steps, state = q.popleft()
        if state in seen:
            continue
        if is_solution(state):
            return steps
        q.extend((steps + 1, s) for s in next_states(state))
        seen.add(state)
    assert False


def parse(txt: str, *, extra_items: bool = False) -> tuple[tuple[int, int], ...]:
    pairs: dict[str, tuple[int, int]] = {}
    for floor, s in enumerate(txt.splitlines()):
        words = s.split()
        for i, word in enumerate(words):
            word = word.strip(",.")
            if word in ITEM_TYPES:
                atom = words[i - 1].split("-")[0]
                pair = pairs.get(atom, (-999, -999))
                pos = tuple(floor if word == ITEM_TYPES[j] else pair[j] for j in range(2))
                assert len(pos) == 2
                pairs[atom] = pos
    if extra_items:
        for element in NEW_ELEMENTS:
            pairs[element] = (0, 0)
    return tuple(sorted(pairs.values()))


State = tuple[int, tuple[tuple[int, int], ...]]


def next_states(state: State) -> set[State]:
    next_states = set[State]()

    movable_items = items_on_floor(*state)

    for item in movable_items:
        next_states.update(next_states_helper(state, (item,)))

    for items in itertools.combinations(movable_items, r=2):
        next_states.update(next_states_helper(state, items))

    safe_states = {s for s in next_states if is_safe(s)}
    return safe_states


def next_states_helper(state: State, items_to_move: Sequence[tuple[int, int]]) -> Generator[State, None, None]:
    pos, item_pairs = state
    for new_pos in (pos + delta for delta in (-1, 1) if pos + delta in range(NUM_FLOORS)):
        yield (new_pos, new_item_pairs(item_pairs, items_to_move, new_pos))


def new_item_pairs(
    item_pairs: tuple[tuple[int, int], ...],
    items_to_move: Sequence[tuple[int, int]],
    destination: int,
) -> tuple[tuple[int, int], ...]:
    new = [*item_pairs]
    for pair_i, item_i in items_to_move:
        lst = list(new[pair_i])
        lst[item_i] = destination
        tup = tuple(lst)
        assert len(tup) == 2
        new[pair_i] = tup
    return tuple(sorted(new))


def items_on_floor(floor: int, item_pairs: tuple[tuple[int, int], ...]) -> set[tuple[int, int]]:
    return {
        (pair_i, item_i)
        for pair_i, item_pair in enumerate(item_pairs)
        for item_i, location in enumerate(item_pair)
        if location == floor
    }


def is_safe(state: State) -> bool:
    # if a chip is ever left in the same area as another RTG,
    # and it's not connected to its own RTG, the chip will be fried
    _pos, item_locs = state
    return all(floor_is_safe(floor, item_locs) for floor in range(NUM_FLOORS))


def floor_is_safe(floor: int, item_locs: tuple[tuple[int, int], ...]) -> bool:
    items = items_on_floor(floor, item_locs)
    generators = {i[0] for i in items if i[1] == 0}
    if len(generators) > 0:
        microchips = {i[0] for i in items if i[1] == 1}
        unpaired_microchips = microchips - generators
        if len(unpaired_microchips) > 0:
            return False
    return True


def is_solution(state: State) -> bool:
    pos, item_pairs = state
    return pos == NUM_FLOORS - 1 and all(loc == NUM_FLOORS - 1 for pair in item_pairs for loc in pair)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
