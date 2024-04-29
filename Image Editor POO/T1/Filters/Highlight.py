from Filters.Filter import Filter

class Highlight(Filter):
    def __init__(self, position, db, R, G, B, Tolerance):
        super().__init__(position, db)
        self.Pxls = self.Img.load()
        self.ValueR = R
        self.ValueG = G
        self.ValueB = B
        self.Tolerance = Tolerance
        
    def Apply(self):
        for j in range(self.Img.size[1]):
            for i in range(self.Img.size[0]):
                if(((self.ValueR-self.Tolerance) < self.Pxls[i, j][0] < (self.ValueR+self.Tolerance)) and ((self.ValueG-self.Tolerance) < self.Pxls[i, j][1] < (self.ValueG+self.Tolerance)) and ((self.ValueB-self.Tolerance) < self.Pxls[i, j][2] < (self.ValueB+self.Tolerance))):
                    ...
                else:
                    self.Pxls[i, j] = (int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3), int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3), int((self.Pxls[i, j][0] + self.Pxls[i, j][1] + self.Pxls[i, j][2])/3))