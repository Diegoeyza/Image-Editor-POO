from Filters.Filter import Filter
from PIL import ImageDraw

class Draw_SmileyFace(Filter):
    def __init__(self, position, db, x, y, color, size):
        super().__init__(position, db)
        self.Color=color
        self.Imgx=x
        self.Imgy=y
        self.Size=size

    def Apply(self):
        Draw = ImageDraw.Draw(self.Img)
        Draw.ellipse([(self.Imgx+(self.Size*0.2), self.Imgy+(self.Size*0.2)), (self.Imgx+(self.Size*0.4), self.Imgy+(self.Size*0.5))], fill=None, outline=self.Color)
        Draw.ellipse([(self.Imgx+(self.Size*0.6), self.Imgy+(self.Size*0.2)), (self.Imgx+(self.Size*0.8), self.Imgy+(self.Size*0.5))], fill=None, outline=self.Color)
        Draw.pieslice([(self.Imgx+(self.Size*0.2), self.Imgy+(self.Size*0.4)), (self.Imgx+(self.Size*0.8), self.Imgy+(self.Size*0.8))], start=0, end=-180, outline=self.Color)
        Draw.ellipse([(self.Imgx, self.Imgy), (self.Imgx+self.Size, self.Imgy+self.Size)], None, self.Color)