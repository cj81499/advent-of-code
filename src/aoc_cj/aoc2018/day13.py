from dataclasses import dataclass

ARROW_TO_DIRECTION = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

DIRECTION_TO_ARROW = {v: k for k, v in ARROW_TO_DIRECTION.items()}


@dataclass
class Cart:
    x: int
    y: int
    dx: int
    dy: int
    intersection_count = 0

    def turn_right(self):
        self.dx, self.dy = -self.dy, self.dx

    def turn_left(self):
        self.dx, self.dy = self.dy, -self.dx

    def arrow(self):
        return DIRECTION_TO_ARROW[(self.dx, self.dy)]

    def move(self, track):
        self.x += self.dx
        self.y += self.dy
        p = (self.x, self.y)
        track_under_cart = track[p]
        if track_under_cart == "+":
            if self.intersection_count % 3 == 0:
                self.turn_left()
            elif self.intersection_count % 3 == 2:
                self.turn_right()
            self.intersection_count += 1
        elif track_under_cart == "/":
            if self.dx == 0:
                self.turn_right()
            else:
                self.turn_left()
        elif track_under_cart == "\\":
            if self.dx == 0:
                self.turn_left()
            else:
                self.turn_right()
        return p


class Simulation:
    def __init__(self, lines):
        self.track = {}
        self.carts = {}
        self.height = len(lines)
        self.width = max(len(line) for line in lines)
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                p = (x, y)
                if c in "+-|/\\":
                    self.track[p] = c
                elif c in "^v<>":
                    dx, dy = ARROW_TO_DIRECTION[c]
                    self.carts[p] = Cart(x, y, dx, dy)
                    self.track[p] = "|" if dx == 0 else "-"

    @staticmethod
    def check_for_crash(dict_to_check, p, crash):
        try:
            del dict_to_check[p]
            return True
        except KeyError:
            return crash

    def move_carts(self, partb=False):
        crashes = []
        new_carts = {}
        for y in range(self.height):
            for x in range(self.width):
                p = (x, y)
                if p in self.carts:
                    cart = self.carts[p]
                    del self.carts[p]
                    p = cart.move(self.track)
                    crash = self.check_for_crash(new_carts, p, False)
                    crash = self.check_for_crash(self.carts, p, crash)
                    if not crash:
                        new_carts[p] = cart
                    else:
                        crashes.append(p)
        self.carts = new_carts
        return crashes, self.carts

    def __str__(self):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                p = (x, y)
                if p in self.carts:
                    s += self.carts[p].arrow()
                elif p in self.track:
                    s += self.track[p]
                else:
                    s += " "
            if y != self.height - 1:
                s += "\n"
        return s


def parta(txt):
    s = Simulation(txt.splitlines())
    crashes = []
    while len(crashes) != 1:
        crashes, _ = s.move_carts()
    return ",".join(map(str, crashes[0]))


def partb(txt):
    s = Simulation(txt.splitlines())
    carts = [None, None]
    while len(carts) > 1:
        crashes, carts = s.move_carts(partb=True)
    return ",".join(map(str, [*carts][0]))


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
