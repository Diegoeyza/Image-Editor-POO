from Filters import Draw_line
from PIL import Image
from Intermediary import FilterIntermediary
from typing import Optional
import re

class InterDrawLine(FilterIntermediary):
    @classmethod
    def get_description(cls):
        return "Draw line" 

    @classmethod
    def ask_params(cls, position: Optional[int]=None, db: Optional[dict]=None):
        ColorChoice = input("\nSelect a color:\n1- Blue\n2- Red\n3- Black\n4- White\n5- Green\n6- Pink\n--> ")
        if (ColorChoice == "1"):
            cls.Color = (0,0,255)
        elif (ColorChoice == "2"):
            cls.Color = (255,0,0)
        elif (ColorChoice == "3"):
            cls.Color = (0,0,0)
        elif (ColorChoice == "4"):
            cls.Color = (255,255,255)
        elif (ColorChoice == "5"):
            cls.Color = (0,255,0)
        else:
            cls.Color = (200,0,200)
        Img=Image.open(db[position]).convert('RGB')
        print(f"Current image size is {Img.width}x{Img.height}")
        print("Select x and y coordinate for starting point (x coordinates are from left to right, y coordinates from top to bottom)")
        cls.Imgx0 = int(input("x: "))
        cls.Imgy0 = int(input("y: "))
        print("Select x and y for ending point, x and y must be bigger than the last x and y coordinates correspondingly")
        cls.Imgx1 = int(input("x: "))
        cls.Imgy1 = int(input("y: "))
        cls.Width = int(input("Select line width in pixels\n>"))

    @classmethod
    def create_action(cls,position,db):
        return Draw_line(position, db, cls.Color, cls.Imgx0, cls.Imgy0, cls.Imgx1, cls.Imgy1, cls.Width)

    @classmethod
    def params(cls):
        return(f"Draw line; {cls.Color}; {cls.Imgx0}; {cls.Imgy0}; {cls.Imgx1}; {cls.Imgy1}; {cls.Width}")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        tup=re.sub("[()]","",commands[1])
        tup=tuple(map(int,tup.split(",")))
        action = Draw_line(position, dictionary.Dict["File"], tup)
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])
        dictionary.Change(f"Draw line; {tup}", dictionary.Dict["File"][position], position)