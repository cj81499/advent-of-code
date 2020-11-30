import numpy as np
from tqdm import tqdm


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


def part1(serial):
    fuel_cells = build_fuel_cells(serial)

    max_power = 0
    max_coords = None
    for y in range(300 - 3):
        for x in range(300 - 3):
            power = np.sum(fuel_cells[y:y + 3, x:x + 3])
            if power > max_power:
                max_power = power
                max_coords = (x, y)

    return ",".join([str(x) for x in max_coords])


def part2(serial):
    fuel_cells = build_fuel_cells(serial)

    max_power = 0
    max_coords = None
    no_change_counter = 0
    for z in range(1, 300):
        prev_max_coords = max_coords
        if no_change_counter > 5:
            break
        for y in range(300 - z):
            for x in range(300 - z):
                power = np.sum(fuel_cells[y:y + z, x:x + z])
                if power > max_power:
                    max_power = power
                    max_coords = (x, y, z)
        if prev_max_coords == max_coords:
            no_change_counter += 1
        else:
            no_change_counter = 0
        # print(f"{z}: {max_power} @ {max_coords}")
    return ",".join([str(x) for x in max_coords])


def partial_sum_table(table):
    par_sum_tab = np.zeros_like(table)
    for y, row in enumerate(table):
        for x, i in enumerate(row):
            left = par_sum_tab[y, x - 1] if x > 0 else 0
            above = par_sum_tab[y - 1, x] if y > 0 else 0
            above_left = par_sum_tab[y - 1, x - 1] if x > 0 and y > 0 else 0
            par_sum_tab[y, x] = (left+above)-above_left+i
    return par_sum_tab


def sum_of_area(t, x, y, sq_size):
    top_left = t[y - 1, x - 1] if y - 1 >= 0 and x - 1 >= 0 else 0
    top_right = t[y - 1, x + sq_size - 1] if y - 1 >= 0 else 0
    bottom_left = t[y + sq_size - 1, x - 1] if x - 1 >= 0 else 0
    bottom_right = t[y + sq_size - 1, x + sq_size - 1]
    return top_left + bottom_right - (top_right + bottom_left)


def part2_polished(serial):
    fuel_cells = build_fuel_cells(serial)
    part_sum_table = partial_sum_table(fuel_cells)
    max_coords = None
    max_power = 0
    for sq_size in tqdm(range(1, 301), leave=False, ascii=True):
        for y in range(300 - sq_size):
            for x in range(300 - sq_size):
                s = sum_of_area(part_sum_table, x, y, sq_size)
                if s > max_power:
                    max_power = s
                    max_coords = (x, y, sq_size)
    return ",".join([str(x) for x in max_coords])


def main():
    input_txt, _ = helpers.load_input(11, "Chronal Charge")

    serial = int(input_txt)

    print(f"part1: {part1(serial)}")
    # print(f"part2: {part2(serial)}")
    print(f"part2_polished: {part2_polished(serial)}")


if __name__ == "__main__":
    import helpers
    main()
