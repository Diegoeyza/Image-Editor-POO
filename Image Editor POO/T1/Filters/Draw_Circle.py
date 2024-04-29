from Filters.Filter import Filter
from PIL import ImageDraw

class Draw_circle(Filter):
    def __init__(self, position, db, color, x, y, rad, width):
        super().__init__(position, db)
        self.Color=color
        self.Imgx=x
        self.Imgy=y
        self.Rad=rad
        self.Width = width

    def Apply(self):
        Draw = ImageDraw.Draw(self.Img)
        Draw.ellipse([(self.Imgx-self.Rad, self.Imgy-self.Rad), (self.Imgx+self.Rad, self.Imgy+self.Rad)], None, outline=self.Color, width=self.Width)
