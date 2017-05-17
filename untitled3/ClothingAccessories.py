from Clothes import Clothes

class ClothingAccessories(Clothes):
    carried=""
    warm=""
    def __init__(self, color, size, material, carried, warm):
        super(ClothingAccessories, self).__init__(color, size, material)
        self.carried=carried
        self.warm=warm

    def getcolor(self):
        return self.color

    def getsize(self):
        return self.size

    def getmaterial(self):
        return self.material

    def getcarried(self):
        return self.carried

    def getwarm(self):
        return self.warm
