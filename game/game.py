from res.models import *


class Game:
    mine: Mine
    player: Player

    def __init__(self, length: int = None, width: int = None):
        mine_map = [[0] * width] * length
        self.mine = Mine(length=length, width=width, map=mine_map)
        self.player = Player()

    def show_mine(self):
        for i in range(self.mine.length):
            for j in range(self.mine.width):
                print(self.mine.map[i][j])