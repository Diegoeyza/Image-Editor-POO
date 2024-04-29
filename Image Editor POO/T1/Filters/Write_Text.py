from Filters.Filter import Filter
from PIL import ImageDraw

class Write_text(Filter):
    def __init__(self, position, db, x, y, text, color, size):
        super().__init__(position, db)
        self.x=x
        self.y=y
        self.text=text
        self.Color=color
        self.size=size

    def Apply(self):
        Draw = ImageDraw.Draw(self.Img)
        Draw.text((self.x, self.y), self.text, self.Color, font_size=self.size)