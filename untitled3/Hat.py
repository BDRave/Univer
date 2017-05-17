from Clothes import Clothes


class Hat(Clothes):

    season=""

    def __init__(self, color, size, material, season):
        super(Hat, self).__init__(color, size, material)
        self.season = season

    def getseason(self):
        return self.season


