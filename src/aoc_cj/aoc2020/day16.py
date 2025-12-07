import functools
import operator

import more_itertools as mi


def is_valid_ticket(ticket, fields):
    for n in ticket:
        if not any(n in r for f in fields.values() for r in f):
            return False, n
    return True, 0


def parse_field(field_str):
    name, ranges_str = field_str.split(": ")
    ranges = []
    for r in ranges_str.split(" or "):
        start, stop = (int(x) for x in r.split("-"))
        ranges.append(range(start, stop + 1))
    return name, tuple(ranges)


def parse_ticket(ticket_str):
    return tuple(int(x) for x in ticket_str.split(","))


def parse_input(txt):
    fields_str, my_ticket, nearby_tickets = txt.split("\n\n")
    fields = dict([parse_field(f) for f in fields_str.splitlines()])
    my_ticket = parse_ticket(my_ticket.splitlines()[1])
    nearby_tickets = {parse_ticket(t) for t in nearby_tickets.splitlines()[1:]}
    return fields, my_ticket, nearby_tickets


def part_1(txt):
    fields, _my_ticket, nearby_tickets = parse_input(txt)
    return sum(is_valid_ticket(t, fields)[1] for t in nearby_tickets)


def get_actual_fields(fields, my_ticket, nearby_tickets):
    position_possibile_fields = tuple(set(fields) for _ in range(len(my_ticket)))

    # for each valid ticket
    for t in {t for t in nearby_tickets if is_valid_ticket(t, fields)[0]}:
        # for each value on the ticket and list of possible fields at the location of that value
        for ticket_value, possibile_fields in zip(t, position_possibile_fields, strict=True):
            for f in set(possibile_fields):
                # if the value is not valid for one of the possible fields, remove it as a possibility
                if not any(ticket_value in r for r in fields[f]):
                    possibile_fields.remove(f)

    # while there are one or more positions that have more than multiple possibilites
    while any(len(x) > 1 for x in position_possibile_fields):
        # get the names of fields that we know are correct (they're the only possibility at a location)
        solved_fields = {mi.one(p) for p in position_possibile_fields if len(p) == 1}
        # remove those fields as possibilities for everywhere else
        for f in solved_fields:
            for p in position_possibile_fields:
                if len(p) > 1 and f in p:
                    p.remove(f)

    return tuple(x.pop() for x in position_possibile_fields)


def part_2(txt):
    fields, my_ticket, nearby_tickets = parse_input(txt)
    actual_fields = get_actual_fields(fields, my_ticket, nearby_tickets)
    departure_values = [
        val for val, field_name in zip(my_ticket, actual_fields, strict=True) if "departure" in field_name
    ]
    return functools.reduce(operator.mul, departure_values, 1)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
