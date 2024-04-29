from Filters.Filter import Filter
from PIL import Image

class Reflect_Y(Filter):
    def __init__(self, position, db):
        super().__init__(position,db)

    def Apply(self):
        self.Img=self.Img.transpose(Image.FLIP_LEFT_RIGHT)

class Reflect_X(Filter):
    def __init__(self, position, db):
        super().__init__(position,db)

    def Apply(self):
        self.Img=self.Img.transpose(Image.FLIP_TOP_BOTTOM)