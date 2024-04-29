from Filters.Filter import Filter


class Resize(Filter):
    def __init__(self, position, db, width, height):
        super().__init__(position,db)
        self.width=width
        self.height=height

    def Apply(self):
        self.Img = self.Img.resize((self.width, self.height))
        