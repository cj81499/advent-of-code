import parse

parser = parse.compile("Step {} must be finished before step {} can begin.")


class Task:
    def __init__(self, name, offset):
        self.name = name
        self.before = set()
        self.after = set()
        self.running = False
        self.remaining_time = ord(name) - ord("A") + 1 + offset

    def __str__(self):
        return str(f"{self.name}: ({self.running}, {self.remaining_time}) ({self.before}, {self.after})")


def get_first(tasks: dict):
    no_before = set()
    for n in tasks:
        if len(tasks[n].before) == 0:
            no_before.add(n)
    return min(no_before)


def remove_task(tasks: dict, t):
    for n in tasks[t].after:
        tasks[n].before.remove(t)
    del tasks[t]


def lines_to_tasks(lines, offset=60):
    tasks = {}

    # Fill in tasks dictionary
    for l in lines:
        before, after = parser.parse(l).fixed
        tasks.setdefault(before, Task(before, offset))
        tasks.setdefault(after, Task(after, offset))
        tasks[before].after.add(after)
        tasks[after].before.add(before)

    return tasks


def startable_tasks(tasks, workers):
    startable = []
    for t in tasks:
        if len(tasks[t].before) == 0 and t not in workers:
            startable.append(t)
    # NOTE: I'm not certain this needs to be sorted. It"s a pretty
    # insignificant operation in the context of the problem, so I"ll
    # leave it cuz it works.
    return sorted(startable)


def add_new_tasks_if_possible(tasks, workers):
    startable = startable_tasks(tasks, workers)
    for i, w in enumerate(workers):
        if len(startable) == 0:
            break
        if w is None:
            workers[i] = startable.pop(0)


def part1(lines: list):
    tasks = lines_to_tasks(lines)

    # Find order
    order = []
    while len(tasks) > 0:
        first = get_first(tasks)
        order.append(first)
        remove_task(tasks, first)

    return "".join(order)


def part2(lines: list, offset=60, helper_count=4):
    tasks = lines_to_tasks(lines, offset)

    workers = [None for _ in range(helper_count + 1)]
    elapsed_time = 0
    add_new_tasks_if_possible(tasks, workers)
    incomplete = True
    while incomplete:
        for i, t in enumerate(workers):
            if t is not None:
                tasks[t].remaining_time -= 1
                if tasks[t].remaining_time == 0:
                    remove_task(tasks, t)
                    workers[i] = None
        add_new_tasks_if_possible(tasks, workers)
        elapsed_time += 1
        incomplete = not all([tasks[t].remaining_time == 0 for t in tasks])
    return elapsed_time


def main():
    _, input_lines = helpers.load_input(7, "The Sum of Its Parts")

    print(f"part1: {part1(input_lines)}")
    print(f"part2: {part2(input_lines)}")


if __name__ == "__main__":
    import helpers
    main()
