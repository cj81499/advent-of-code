import itertools


def n_th_element(n, gen):
    for _ in range(n - 1):
        next(gen)
    return next(gen)


def transform(subject_number):
    pk = 1
    while True:
        pk *= subject_number
        pk %= 20201227
        yield pk


def parta(txt):
    card_pk, door_pk = tuple(map(int, txt.splitlines()))

    card_loop_size = None
    door_loop_size = None

    primary_keys = transform(7)

    for loop_size, pk in zip(itertools.count(1), primary_keys):
        # save loop_size if we've found the associated pk
        if pk == card_pk:
            card_loop_size = loop_size
        if pk == door_pk:
            door_loop_size = loop_size

        if card_loop_size is not None and door_loop_size is not None:
            break

    # calculate whichever will have fewer loops
    if door_loop_size < card_loop_size:
        return n_th_element(door_loop_size, transform(card_pk))
    return n_th_element(card_loop_size, transform(door_pk))


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
