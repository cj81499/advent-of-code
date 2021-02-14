from __future__ import annotations


def bridges_helper(components, bridge_so_far):
    yield bridge_so_far
    free_port = bridge_so_far[-1][-1]
    can_connect = [c for c in components if free_port in c]
    for component in can_connect:
        components.remove(component)
        a, b = component
        bridge_so_far.append((free_port, a if b == free_port else b))
        yield from bridges_helper(components, bridge_so_far)
        bridge_so_far.pop()
        components.append(component)


def bridges(components):
    start_components = [c for c in components if 0 in c]
    for start_component in start_components:
        components.remove(start_component)
        yield from bridges_helper(components, [tuple(sorted(start_component))])
        components.append(start_component)


def strength(bridge):
    return sum(sum(c) for c in bridge)


def parta(txt: str):
    components = [tuple(sorted(int(n) for n in line.split("/"))) for line in txt.splitlines()]
    return max(strength(b) for b in bridges(components))


def partb(txt: str):
    components = [tuple(sorted(int(n) for n in line.split("/"))) for line in txt.splitlines()]
    return max((len(b), strength(b)) for b in bridges(components))[1]


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
