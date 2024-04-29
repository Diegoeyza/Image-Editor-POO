from Compositions.Composition import Composition
from PIL import Image
from Database import FileCheck

class Paste_Right(Composition):
    def __init__(self, position, db, filename2):
        super().__init__(position, db)
        self.filename2 = filename2

    def Apply(self):
        self.Img2 = Image.open(self.filename2).convert('RGB')  
        self._size1 = [(self.Img).width,(self.Img).height]
        print((self.Img).width)
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', (self._size2[0]+self._size1[0],max(self._size2[1],self._size1[1])))

        (self.background).paste(self.Img,(0,0))
        (self.background).paste(self.Img2,(self._size1[0]+1,0))
        self.Img = self.background

class Paste_Left(Composition):
    def __init__(self, position, db, filename2):
        super().__init__(position, db)
        self.filename2 = filename2

    def Apply(self):
        self.Img2 = Image.open(self.filename2).convert('RGB')  
        self._size1 = [(self.Img).width,(self.Img).height]
        print((self.Img).width)
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', (self._size2[0]+self._size1[0],max(self._size2[1],self._size1[1])))

        (self.background).paste(self.Img2,(0,0))
        (self.background).paste(self.Img,(self._size2[0]+1,0))
        self.Img = self.background

class Paste_Below(Composition):
    def __init__(self, position, db, filename2):
        super().__init__(position, db)
        self.filename2 = filename2

    def Apply(self):
        self.Img2 = Image.open(self.filename2).convert('RGB')
        self._size1 = [(self.Img).width,(self.Img).height]
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', (max(self._size2[0],self._size1[0]), self._size2[1]+self._size1[1]))

        (self.background).paste(self.Img,(0,0))
        (self.background).paste(self.Img2,(0,self._size1[1]+1))
        self.Img = self.background
  
class Paste_Over(Composition):
    def __init__(self, position, db, filename2):
        super().__init__(position, db)
        self.filename2 = filename2
        
    def Apply(self):
        self.Img2 = Image.open(self.filename2).convert('RGB')  
        self._size1 = [(self.Img).width,(self.Img).height]
        self._size2=[(self.Img2).width,(self.Img2).height]
        self.background=Image.new('RGB', (max(self._size2[0],self._size1[0]), self._size2[1]+self._size1[1]))

        (self.background).paste(self.Img2,(0,0))
        (self.background).paste(self.Img,(0,self._size2[1]+1))
        self.Img = self.background
    