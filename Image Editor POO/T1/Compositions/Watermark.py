from PIL import Image
from Compositions.Composition import Composition
from Database import FileCheck

class Watermark(Composition):
    def __init__(self, position, db, filename2):
        super().__init__(position, db)
        self.filename2 = filename2

    def Apply(self):
        self.Img2 = Image.open(self.filename2).convert('RGB')
        self.Pxls1 = (self.Img).load()
        self.Img2 = (self.Img2).resize((((self.Img).size)[0], ((self.Img).size)[1]))
        self.Pxls2 = (self.Img2).load()
        
        for j in range(((self.Img).size)[1]):
            for i in range(((self.Img).size)[0]):
                (self.Pxls1)[i, j] = (int(((((self.Pxls1)[i, j])[0])*0.7 + (((self.Pxls2)[i, j])[0])*0.3)), int(((((self.Pxls1)[i, j])[1])*0.7 + (((self.Pxls2)[i, j])[1])*0.3)), int(((((self.Pxls1)[i, j])[2])*0.7 + (((self.Pxls2)[i, j])[2])*0.3)))