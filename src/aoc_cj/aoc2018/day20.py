from collections import deque

DIRECTIONS = {"N": (0, -1), "W": (-1, 0), "S": (0, 1), "E": (1, 0)}
OPPOSITE_DIRECTION = {"N": "S", "W": "E", "S": "N", "E": "W"}


class Facility:
    class Room:
        def __init__(self, data=".", dist=0):
            self.dist = dist
            self.middle = str(data)[0]
            self.doors = {"N": False, "W": False, "S": False, "E": False}

        def add_door(self, direction):
            self.doors[direction] = True

        def _door_str(self, direction):
            return ("-" if direction in "NS" else "|") if self.doors[direction] else "?"

        def __str__(self):
            s = (
                "#"
                + self._door_str("N")
                + "#,"
                + self._door_str("W")
                + self.middle
                + self._door_str("E")
                + ",#"
                + self._door_str("S")
                + "#"
            )
            return s

    def __init__(self, regex):
        self.regex = deque(list(regex))
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
        self.f = {}

        self.fill_in_map()

    def update_mins_and_maxes(self, pos):
        x, y = pos
        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)

    def move(self, pos, direction):
        x, y = pos
        dx, dy = DIRECTIONS[direction]
        new_pos = (x + dx, y + dy)
        self.update_mins_and_maxes(new_pos)
        return new_pos

    def addRoom(self, pos, dir_of_movement):
        x, y = pos
        dx, dy = DIRECTIONS[dir_of_movement]
        prev_pos = (x - dx, y - dy)
        prev_room = self.f[prev_pos]
        prev_room.add_door(dir_of_movement)

        if pos not in self.f:
            r = Facility.Room(".", prev_room.dist + 1)
            self.f[pos] = r
        self.f[pos].add_door(OPPOSITE_DIRECTION[dir_of_movement])

    def _explore_chunk_list(self, pos, chunk_list):
        end_positions = set()
        for chunk in chunk_list:
            for end_p in self._explore_chunk(pos, chunk):
                end_positions.add(end_p)
        return end_positions

    def _explore_chunk(self, pos, chunk):
        start_positions = set(pos)
        for chunk_part in chunk:
            end_positions = set()
            for p in start_positions:
                if isinstance(chunk_part, str):
                    end_positions.add(self._explore_dir_str(p, chunk_part))
                else:
                    for end_p in self._explore_chunk_list([p], chunk_part):
                        end_positions.add(end_p)
            start_positions = end_positions
        return start_positions

    def _explore_dir_str(self, pos, dir_str):
        current_pos = pos
        for _dir in dir_str:
            current_pos = self.move(current_pos, _dir)
            self.addRoom(current_pos, _dir)
        return current_pos

    @staticmethod
    def parse_dir_str(q):
        if not q[0] in "NSWE":
            raise AssertionError("dir-str must start with a direction")
        dir_str = deque()
        while q[0] in "NSWE":
            dir_str.append(q.popleft())  # add dir to dir-str
        return "".join(dir_str)

    @staticmethod
    def parse_paren(q):
        if q[0] != "(":
            raise AssertionError('paren must start with "("')

        q.popleft()  # remove "("
        while q[0] in "NSWE":
            paren = Facility.parse_chunk_list(q)

        if q[0] != ")":
            raise AssertionError('paren must end with "("')
        q.popleft()  # remove "("
        return paren

    @staticmethod
    def parse_chunk(q):
        chunk = deque()
        while q[0] in "NSWE(":
            if q[0] == "(":
                chunk.append(Facility.parse_paren(q))
            else:
                chunk.append(Facility.parse_dir_str(q))
        return list(chunk)

    @staticmethod
    def parse_chunk_list(q):
        chunk_list = deque()
        chunk_list.append(Facility.parse_chunk(q))
        while q[0] == "|":
            q.popleft()  # remove "|"
            chunk_list.append(Facility.parse_chunk(q))
        return list(chunk_list)

    @staticmethod
    def parse_regex(q):
        if q[0] != "^":
            raise AssertionError('regex must start with " ^ "')
        q.popleft()  # remove "^"
        regex = Facility.parse_chunk_list(q)
        if q[0] != "$":
            raise AssertionError('regex must end with "$"')
        q.popleft()  # remove "$"
        return regex

    def fill_in_map(self):
        pos = (0, 0)
        self.f[pos] = Facility.Room("X")
        parsed_regex = Facility.parse_regex(self.regex)
        self._explore_chunk_list([pos], parsed_regex)

    def __str__(self):
        s = "#" + "?#" * (self.max_x - self.min_x + 1) + "\n"
        for y in range(self.min_y, self.max_y + 1):
            middle = []
            bottom = []
            for x in range(self.min_x, self.max_x + 1):
                pos = (x, y)
                if pos in self.f:
                    r_m, r_b = str(self.f[pos]).split(",")[1:]
                    middle.append(r_m[1:])
                    bottom.append(r_b[1:])
                else:
                    middle.append("  ")
                    bottom.append("  ")
            s += "?" + "".join(middle) + "\n"
            s += "#" + "".join(bottom) + "\n"
        return s.strip().replace("?", "#")

    def furthest_room_dist(self):
        max_dist = 0
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                r = self.f[(x, y)]
                if r.dist > max_dist:
                    max_dist = r.dist
        return max_dist

    def count_rooms_at_least_dist_far(self, dist):
        count = 0
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                r = self.f[(x, y)]
                if r.dist >= dist:
                    count += 1
        return count


def part_1(txt):
    fac = Facility(txt)
    return fac.furthest_room_dist()


def part_2(txt):
    fac = Facility(txt)
    return fac.count_rooms_at_least_dist_far(1000)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
