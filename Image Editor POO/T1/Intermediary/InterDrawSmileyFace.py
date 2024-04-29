from typing import Optional
from PIL import Image
from Intermediary import FilterIntermediary
from Filters import Draw_SmileyFace
import re

class InterDrawSmileyFace(FilterIntermediary):
    @classmethod
    def get_description(cls):
        return("Draw a smiling face")

    @classmethod
    def ask_params(cls, position: Optional[int], db: Optional[dict]):
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
        print("Select x and y coordinate for the smiley face's box top left corner (From upper left corner)")
        cls.Imgx = int(input("x: "))
        cls.Imgy = int(input("y: "))
        cls.Size = int(input("Select size in pixels\n>"))

    @classmethod
    def create_action(cls, position, db):
        return Draw_SmileyFace(position, db, cls.Imgx, cls.Imgy, cls.Color, cls.Size)
    
    @classmethod
    def params(cls):
        return(f"Draw a smiling face; {cls.Imgx}; {cls.Imgy}; {cls.Color}; {cls.Size}")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        tup=re.sub("[()]","",commands[3])
        tup=tuple(map(int,tup.split(",")))
        action = Draw_SmileyFace(position, dictionary.Dict["File"], int(commands[1]), int(commands[2]), tup, int(commands[4]))
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])
        dictionary.Change(f"Draw a smiling face; {commands[1]}; {commands[2]}; {tup}; {commands[4]}", dictionary.Dict["File"][position], position)
