import random


class Mine:
    _length: int
    _width: int
    _map: [int]

    def __init__(self):
        self._length = 100
        self._width = 100
        self._map = []

    def create_mine(self) -> None:
        for x in range(0, self._width):
            for y in range(0, self._length):
                self._map[x][y] = random.randint(0, 1)

    def set_pos(self, x: int, y: int):
        self._map[x][y] = -1
