import collections  # noqa
import itertools  # noqa
import re  # noqa


def simulate(cups, moves):
    # setup
    # we need len(cups) + 1 elements b/c arr[0] will always be None
    arr = [None] * (len(cups) + 1)  # arr[n] == cup that follows n
    prev = cups[-1]
    for cup in cups:
        arr[prev] = cup
        prev = cup

    min_cup, max_cup = min(cups), max(cups)

    # simulate
    current = cups[0]
    for i in range(moves):
        # pick up 3 cups
        picked_up = []
        to_pick_up = current
        for j in range(3):
            picked_up.append(arr[to_pick_up])
            to_pick_up = picked_up[-1]
        # make current point past picked up cups.
        # they will be reinserted later
        arr[current] = arr[picked_up[-1]]

        # get destination cup
        destination = current - 1
        while destination in picked_up or destination < min_cup:
            destination -= 1
            if destination < min_cup:
                destination = max_cup

        # put picked up cups into new position
        arr[picked_up[-1]] = arr[destination]
        arr[destination] = picked_up[0]

        # update current
        current = arr[current]

    return arr


def parta(txt):
    cups = list(map(int, txt))
    results = simulate(cups, 100)

    nums = [results[1]]
    while nums[-1] != 1:
        nums.append(results[nums[-1]])

    return int("".join(map(str, nums[:-1])))


def partb(txt):
    cups = list(map(int, txt))
    cups = list(itertools.chain(cups, range(max(cups) + 1, 1000000 + 1)))
    results = simulate(cups, 10000000)

    # first 2 cups after 1
    first = results[1]
    second = results[first]

    return first * second


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
