from Filters.Filter import Filter
from PIL import ImageDraw

class Draw_line(Filter):
    def __init__(self, position, db, color, imgx0, imgy0, imgx1, imgy1, width):
        super().__init__(position, db)
        self.Color=color
        self.Imx0=imgx0
        self.Imy0=imgy0
        self.Imx1=imgx1
        self.Imy1=imgy1
        self.Width=width
        
    def Apply(self):
        Draw = ImageDraw.Draw(self.Img)
        Draw.line([(self.Imx0, self.Imy0), (self.Imx1, self.Imy1)], fill=(self.Color), width=self.Width)