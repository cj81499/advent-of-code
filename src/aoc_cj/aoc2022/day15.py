import dataclasses


def man_dist(p1: complex, p2: complex) -> float:
    return abs(p1.real - p2.real) + abs(p1.imag - p2.imag)


@dataclasses.dataclass
class Sensor:
    pos: complex
    closest_beacon: complex

    @staticmethod
    def parse(sensor: str) -> "Sensor":
        split = sensor.split()
        p_x = int(split[2].strip("xy=,:"))
        p_y = int(split[3].strip("xy=,:"))
        b_x = int(split[8].strip("xy=,:"))
        b_y = int(split[9].strip("xy=,:"))

        return Sensor(complex(p_x, p_y), complex(b_x, b_y))


def part_1(txt: str, *, y: int = 2000000) -> int:
    sensors = [Sensor.parse(l) for l in txt.splitlines()]

    beacon_positions = {s.closest_beacon for s in sensors}

    cannot_be_beacon = set[complex]()
    for s in sensors:
        m = int(man_dist(s.pos, s.closest_beacon))

        # if the sensor can "see" part of row y
        sensor_y = int(s.pos.imag)
        if sensor_y - m <= y <= sensor_y + m:
            # difference between sensor_y and y
            dy = abs(sensor_y - y)

            # coverage "range" on line y
            dx = m - dy

            sensor_x = int(s.pos.real)
            for x in range(-dx, dx + 1):
                if complex(sensor_x + x, y) not in beacon_positions:
                    cannot_be_beacon.add(sensor_x + x)

    return len(cannot_be_beacon)


def part_2(txt: str, *, max: int = 4000000) -> int:
    # This is quite slow.
    # Might be able to speed it up somewhat by avoiding recomputing man dist
    # between a scanner the and beacon closest to it and avoiding casts from float to int

    x = 0
    y = 0
    sensors = [Sensor.parse(l) for l in txt.splitlines()]

    while True:
        if x > max:
            x = 0
            y += 1

        assert y <= max, "Failed to locate distress beacon before y grew too large."

        for s in sensors:
            m = int(man_dist(s.pos, s.closest_beacon))

            # if the sensor can "see" part of row y
            sensor_y = int(s.pos.imag)
            if sensor_y - m <= y <= sensor_y + m:
                dy = abs(int(s.pos.imag) - y)
                dx = m - dy

                # if sensor can "see" (x, y)
                sensor_x = int(s.pos.real)
                if sensor_x - dx <= x <= sensor_x + dx:
                    # advance x until it's out of the sensor's view
                    x = sensor_x + dx + 1
                    break
        else:
            # If we did not break out of the for loop, no scanner could see
            # (x, y), so that must be the position where the distress
            # beacon is coming from.
            return x * 4000000 + y


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
