from Filters import Write_text
from PIL import Image
from Intermediary import FilterIntermediary
import re

class InterWrite_Text(FilterIntermediary):
    @classmethod
    def get_description(cls):
        return "Write text" 

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
        print("Select x and y coordinate (From upper left corner)")
        cls.x = int(input("x: "))
        cls.y = int(input("y: "))
        cls.size = int(input("Select size in pixels: "))
        cls.text = input("Type in text to be used\n--> ")

    @classmethod
    def create_action(cls,position,db):
        return Write_text(position, db, cls.x, cls.y, cls.text, cls.Color, cls.size)

    @classmethod
    def params(cls):
        return(f"Write text; {cls.x}; {cls.y}; {cls.text}; {cls.Color}; {cls.size}")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        tup=re.sub("[()]","",commands[4])
        tup=tuple(map(int,tup.split(",")))
        action = Write_text(position, dictionary.Dict["File"], int(commands[1]), int(commands[2]), commands[3], tup, int(commands[5]))
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])
        dictionary.Change(f"Write text; {commands[1]}; {commands[2]}; {commands[3]}; {tup}; {commands[5]}", dictionary.Dict["File"][position], position)