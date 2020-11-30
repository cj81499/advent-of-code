from collections import defaultdict
import parse

p = parse.compile("[{}] {}")


def run(events: list):
    guards = defaultdict(lambda: [0 for _ in range(60)])
    active_guard = None  # id of currently active guard
    sleep_start = None  # minute at which sleep begins

    # Strategy 1 (Part 1)
    # Index 0 is the id of the guard that has the most minutes asleep.
    # Index 1 is the duration of sleep
    s1 = [0, 0]

    # Strategy 2 (Part 2)
    # Index 0 is the guard number.
    # Index 1 is the duration of sleep.
    s2 = [0, 0]

    for e in events:
        action = e[1]
        if action[0] == "G":
            active_guard = int(action.split()[1][1:])
            sleep_start = None
        elif action[0] == "f":
            sleep_start = int(e[0][-2:])
        elif action[0] == "w":
            sleep_end = int(e[0][-2:])
            # Update active guard"s sleep counter
            for i in range(sleep_start, sleep_end):
                guards[active_guard][i] += 1
            guard_total_sleep_duration = sum(guards[active_guard])
            guard_max_sleep_duration = max(guards[active_guard])
            if guard_total_sleep_duration > s1[1]:
                s1[1] = guard_total_sleep_duration
                s1[0] = active_guard
            if guard_max_sleep_duration > s2[1]:
                s2[1] = guard_max_sleep_duration
                s2[0] = active_guard

    s1_max_sleep_minute = guards[s1[0]].index(max(guards[s1[0]]))
    part1 = s1_max_sleep_minute * s1[0]

    s2_max_sleep_minute = guards[s2[0]].index(s2[1])
    part2 = s2[0] * s2_max_sleep_minute

    return part1, part2


def events_list(lines):
    events = [p.parse(l).fixed for l in lines]
    events.sort(key=lambda e: e[0])
    return events


def main():
    _, input_lines = helpers.load_input(4, "Repose Record")

    part1, part2 = run(events_list(input_lines))

    print(f"part1: {part1}")
    print(f"part2: {part2}")


if __name__ == "__main__":
    import helpers
    main()
