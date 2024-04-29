from Filters.Filter import Filter
from PIL import ImageDraw

class Draw_Rectangle(Filter):
    def __init__(self, position, db, x0, y0, x1, y1, color, width):
        super().__init__(position, db)
        self.Color=color
        self.Imgx0=x0
        self.Imgy0=y0
        self.Imgx1=x1
        self.Imgy1=y1
        self.width=width
    
    def Apply(self):
        Draw = ImageDraw.Draw(self.Img)
        Draw.rectangle([(self.Imgx0, self.Imgy0), (self.Imgx1, self.Imgy1)], fill=None, outline=self.Color, width=self.width)