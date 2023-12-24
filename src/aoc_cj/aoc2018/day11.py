import numpy as np


def power_level(x, y, serial):
    rack_id = x + 10
    p_l = rack_id * y
    p_l += serial
    p_l *= rack_id
    p_l = (p_l // 100) % 10  # hundreds digit
    return p_l - 5


def build_fuel_cells(serial):
    fuel_cells = np.zeros((300, 300), dtype=int)
    for x in range(len(fuel_cells)):
        for y in range(len(fuel_cells[0])):
            fuel_cells[y, x] = power_level(x, y, serial)
    return fuel_cells


def part_1(txt):
    fuel_cells = build_fuel_cells(int(txt))

    max_power = 0
    max_coords = None
    for y in range(300 - 3):
        for x in range(300 - 3):
            power = np.sum(fuel_cells[y : y + 3, x : x + 3])
            if power > max_power:
                max_power = power
                max_coords = (x, y)

    return ",".join([str(x) for x in max_coords])


def partial_sum_table(table):
    par_sum_tab = np.zeros_like(table)
    for y, row in enumerate(table):
        for x, i in enumerate(row):
            left = par_sum_tab[y, x - 1] if x > 0 else 0
            above = par_sum_tab[y - 1, x] if y > 0 else 0
            above_left = par_sum_tab[y - 1, x - 1] if x > 0 and y > 0 else 0
            par_sum_tab[y, x] = (left + above) - above_left + i
    return par_sum_tab


def sum_of_area(t, x, y, sq_size):
    top_left = t[y - 1, x - 1] if y - 1 >= 0 and x - 1 >= 0 else 0
    top_right = t[y - 1, x + sq_size - 1] if y - 1 >= 0 else 0
    bottom_left = t[y + sq_size - 1, x - 1] if x - 1 >= 0 else 0
    bottom_right = t[y + sq_size - 1, x + sq_size - 1]
    return top_left + bottom_right - (top_right + bottom_left)


def part_2(txt):
    fuel_cells = build_fuel_cells(int(txt))
    part_sum_table = partial_sum_table(fuel_cells)
    max_coords = None
    max_power = 0
    for sq_size in range(1, 301):
        for y in range(300 - sq_size):
            for x in range(300 - sq_size):
                s = sum_of_area(part_sum_table, x, y, sq_size)
                if s > max_power:
                    max_power = s
                    max_coords = (x, y, sq_size)
    return ",".join([str(x) for x in max_coords])


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
