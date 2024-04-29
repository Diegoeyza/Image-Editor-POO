from PIL import Image
from abc import ABC, abstractmethod

class Filter(ABC):
    def __init__(self, position, db):
        self.Img = Image.open(db[position]).convert('RGB')
    
    def show_size(self):
        print(f"Current image size is {self.Img.width}x{self.Img.height}")
    
    @abstractmethod
    def Apply(self):
        ...