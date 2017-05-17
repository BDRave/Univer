from Clothes import Clothes


class Suit(Clothes):

    opened=""
    closed=""

    def __init__(self, color, size, material, opened, closed):
        super(Suit, self).__init__(color, size, material)
        self.opened = opened
        self.closed = closed

    def getopened(self):
        return self.opened

    def getclosed(self):
        return self.closed
