class ClothesManager():
    clothes = []

    def __init__(self, clothes,):
        self.clothes = clothes


    def searchClothes(self, size, color, material):
        for clothe in self.clothes:

            if (clothe.getSize() == size):
                if (clothe.getColor() == color):
                    if (clothe.getMaterial()== material):
                        return clothe;
        return None