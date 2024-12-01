from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def part_1(txt: str):
    network: list[IntcodeProgram] = []
    for network_address in range(50):
        p = IntcodeProgram.parse(txt)
        p.write_input(network_address)
        network.append(p)

    while True:
        for p in network:
            p.run()
            if p.is_waiting_for_input():
                p.write_input(-1)
            p.run()
            if len(p.outputs) > 0:
                assert len(p.outputs) % 3 == 0
                while len(p.outputs) > 0:
                    destination, x, y = (p.outputs.popleft() for _ in range(3))
                    if destination == 255:
                        return y
                    network[destination].write_input(x)
                    network[destination].write_input(y)


def part_2(txt: str):
    network: list[IntcodeProgram] = []
    for network_address in range(50):
        p = IntcodeProgram.parse(txt)
        p.write_input(network_address)
        network.append(p)

    last_y_sent_by_nat = None
    nat = None
    while True:
        packets_sent = 0
        for p in network:
            p.run()
            if p.is_waiting_for_input():
                p.write_input(-1)
            p.run()
            if len(p.outputs) > 0:
                assert len(p.outputs) % 3 == 0
                while len(p.outputs) > 0:
                    packets_sent += 1
                    destination, x, y = (p.outputs.popleft() for _ in range(3))
                    if destination == 255:
                        nat = (x, y)
                    else:
                        network[destination].write_input(x)
                        network[destination].write_input(y)
        is_idle = packets_sent == 0
        if is_idle:
            x, y = nat
            if y == last_y_sent_by_nat:
                return last_y_sent_by_nat
            network[0].write_input(x)
            network[0].write_input(y)
            last_y_sent_by_nat = y


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
