class Clothes:
    size=''
    material=''
    color=0


    def __init__(self,size, material, color):
        self.size = size
        self.material = material
        self.color = color

    def getsize(self):
        return self.size

    def getmaterial(self):
        return self.material

    def getcolor(self):
        return self.color
