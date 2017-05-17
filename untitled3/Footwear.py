from Clothes import Clothes


class Footwear(Clothes):
    impermeability=""

    def __init__(self,color,size,material,impermeability):
        super(Footwear, self).__init__(color,size,material)
        self.impermeability=impermeability

    def getimpermeability(self):
        return self.impermeability



