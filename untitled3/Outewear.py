from Clothes import Clothes


class Outewear(Clothes):
    type=""

    def __init__(self, color, size, material, type):
        super(Outewear, self).__init__(color, size, material)
        self.type = type

    def gettype(self):
        return self.type

