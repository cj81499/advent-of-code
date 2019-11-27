class Grid():
    def __init__(self, dimensions, default_value=None):
        self.grid = {}
        self._default_value = default_value
        for y in range(dimensions[1]):
            for x in range(dimensions[0]):
                self.grid[(x, y)] = self._default_value

    def __getitem__(self, key):
        return self.grid[key]

    def __setitem__(self, key, value):
        self.grid[key] = value

    def __delitem__(self, key):
        self.grid[key] = self._default_value
