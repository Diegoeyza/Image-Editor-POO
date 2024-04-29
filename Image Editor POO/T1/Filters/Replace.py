from Filters.Filter import Filter
from PIL import Image

class Replace(Filter):
    def __init__(self, position, db, r1, g1, b1, tolerance, r2, g2, b2):
        super().__init__(position, db)
        self.r1 = r1
        self.g1 = g1
        self.b1 = b1
        self.tolerance = tolerance
        self.r2 = r2
        self.g2 = g2
        self.b2 = b2
        self.pxls = self.Img.load()

    def Apply(self):
        for j in range(self.Img.size[1]):
            for i in range(self.Img.size[0]):
                if(((self.r1-self.tolerance) < self.pxls[i, j][0] < (self.r1+self.tolerance)) and ((self.g1-self.tolerance) < self.pxls[i, j][1] < (self.g1+self.tolerance)) and ((self.b1-self.tolerance) < self.pxls[i, j][2] < (self.b1+self.tolerance))):
                    self.pxls[i, j] = (self.r2, self.g2, self.b2)