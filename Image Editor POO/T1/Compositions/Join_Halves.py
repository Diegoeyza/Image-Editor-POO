from Compositions.Composition import Composition
from PIL import Image
from Database import FileCheck

class Join_Halves(Composition):
    def __init__(self, position, db, filename2):
        super().__init__(position, db)
        self.filename2 = filename2

    def Apply(self):
        self.Img2 = Image.open(self.filename2).convert('RGB')
        self.Pxls1 = (self.Img).load()
        self.Img2 = (self.Img2).resize((((self.Img).size)[0], ((self.Img).size)[1]))
        self.Pxls2 = (self.Img2).load()

        self._size1 = [(self.Img).width,(self.Img).height]
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', ((self.Img).width,(self.Img).height))

        self.Img_crop = self.Img.crop((0,0, (self.Img).width, int((self.Img).height/2)))
        self.Img2_crop = self.Img2.crop((0,int((self.Img2).height/2), (self.Img).width, (self.Img).height))

        (self.background).paste(self.Img_crop,(0,0))
        (self.background).paste(self.Img2_crop,(0,int((self.Img2).height/2)))
        self.Img = self.background