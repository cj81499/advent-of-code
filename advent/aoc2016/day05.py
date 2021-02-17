import hashlib
import itertools

NUMBER_OF_ZEROS = 5


def password_generator(door_id: str, index_mode=False):
    for i in itertools.count():
        hd = hashlib.md5(f"{door_id}{i}".encode()).hexdigest()
        if hd.startswith("0" * NUMBER_OF_ZEROS):
            x = hd[NUMBER_OF_ZEROS]
            if not index_mode:  # part a
                yield x
            elif x.isnumeric() and (i := int(x)) in range(8):  # part b
                yield i, hd[NUMBER_OF_ZEROS + 1]


def parta(txt: str):
    pass_gen = password_generator(txt)
    return "".join(next(pass_gen) for _ in range(8))


def partb(txt: str):
    pass_gen = password_generator(txt, index_mode=True)
    password = [None] * 8
    while None in password:
        i, x = next(pass_gen)
        if password[i] is None:
            password[i] = x
    return "".join(password)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
