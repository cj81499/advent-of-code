import datetime
import re

PATTERN = re.compile(r"^\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.*)$")


def parta(txt):
    events = events_list(txt.splitlines())
    d = {}
    active_guard = None
    sleep_start = None
    for e in events:
        action = e[1].split()
        if action[0][0] == "G":
            active_guard = int(action[1][1:])
            d.setdefault(active_guard, datetime.timedelta(0))
        elif action[0][0] == "f":
            sleep_start = e[0]
        elif action[0][0] == "w":
            sleep_end = e[0]
            elapsed_time = sleep_end - sleep_start
            d[active_guard] += elapsed_time
    max_sleep_time = datetime.timedelta(0)
    max_sleep_guard = 0
    for g in d:
        if d[g] > max_sleep_time:
            max_sleep_time = d[g]
            max_sleep_guard = g
    sleep_counter = [0 for x in range(60)]
    for e in events:
        action = e[1].split()
        if action[0][0] == "G":
            active_guard = int(action[1][1:])
        elif active_guard == max_sleep_guard and action[0][0] == "f":
            sleep_start = e[0]
        elif active_guard == max_sleep_guard and action[0][0] == "w":
            sleep_end = e[0]
            for i in range(int((sleep_end - sleep_start).total_seconds() // 60)):
                sleep_counter[sleep_start.minute + i] += 1
    return sleep_counter.index(max(sleep_counter)) * max_sleep_guard


def partb(txt):
    events = events_list(txt.splitlines())
    d = {}
    active_guard = None
    sleep_start = None
    for e in events:
        action = e[1].split()
        if action[0][0] == "G":
            active_guard = int(action[1][1:])
            d.setdefault(active_guard, [0 for x in range(60)])
        elif action[0][0] == "f":
            sleep_start = e[0]
        elif action[0][0] == "w":
            sleep_end = e[0]
            for i in range(int((sleep_end - sleep_start).total_seconds() // 60)):
                d[active_guard][sleep_start.minute + i] += 1
    max_sleep_guard = 0
    max_sleep_time = 0
    for guard in d:
        guard_max_sleep_time = max(d[guard])
        if guard_max_sleep_time > max_sleep_time:
            max_sleep_time = guard_max_sleep_time
            max_sleep_guard = guard
    max_sleep_minute = d[max_sleep_guard].index(max_sleep_time)
    return max_sleep_guard * max_sleep_minute


def events_list(lines):
    return sorted(
        (datetime.datetime(*map(int, numbers)), event_str)
        for *numbers, event_str in (PATTERN.match(line).groups() for line in lines)
    )


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
