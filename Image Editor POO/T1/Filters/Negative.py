from Filters.Filter import Filter

class Negative(Filter):
    def __init__(self, position, db):
        super().__init__(position, db)
        self.Pxls = self.Img.load()

    def Apply(self):
        for j in range(self.Img.size[1]):
            for i in range(self.Img.size[0]):
                self.Pxls[i, j] = ((255 - self.Pxls[i, j][0]), (255 - self.Pxls[i, j][1]), (255- self.Pxls[i, j][2]))