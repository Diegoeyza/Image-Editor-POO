from Filters.Filter import Filter
from PIL import Image

class Pixelate(Filter):
    def __init__(self, position, db, Pxl):
        super().__init__(position,db)
        self.Pxl=Pxl

    def Apply(self):
        Shrinked = (self.Img).resize((self.Pxl, self.Pxl), resample=Image.Resampling.BILINEAR)
        (self.Img) = Shrinked.resize((self.Img).size, Image.Resampling.NEAREST)