from Filters import Draw_circle
from PIL import Image
from Intermediary import FilterIntermediary
import re

class InterDrawCirlce(FilterIntermediary):
    @classmethod
    def get_description(cls):
        return "Draw Circle" 

    @classmethod
    def ask_params(cls, position, db):
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
        print("Select x and y coordinates for the circle center (From upper left corner)")
        cls.Imgx = int(input("x: "))
        cls.Imgy = int(input("y: "))
        cls.Rad = int(input("Select radius in pixels: "))
        cls.Width = int(input("Select line width in pixels\n>"))

    @classmethod
    def create_action(cls,position,db):
        return Draw_circle(position, db, cls.Color, cls.Imgx, cls.Imgy, cls.Rad, cls.Width)
    
    @classmethod
    def params(cls):
        return(f"Draw Circle; {cls.Color}; {cls.Imgx}; {cls.Imgy}; {cls.Rad}; {cls.Width}")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        tup=re.sub("[()]","",commands[1])
        tup=tuple(map(int,tup.split(",")))
        action = Draw_circle(position, dictionary.Dict["File"], tup, int(commands[2]), int(commands[3]), int(commands[4]), int(commands[5]))
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])
        dictionary.Change(f"Draw Circle; {tup}; {commands[2]}; {commands[3]}; {commands[4]}; {commands[5]}", dictionary.Dict["File"][position], position)
