from Filters import Reflect_X, Reflect_Y
from Intermediary import FilterIntermediary
from typing import Optional

class InterReflect(FilterIntermediary):
    @classmethod
    def get_description(cls):
        return "Reflect"

    @classmethod
    def ask_params(cls, position: Optional[int]=None, db: Optional[dict]=None):
        a=0
        while (a!=1 and a!=2):
            cls.choice=int(input("\nPlease select the index of the orientation you want to use when reflecting\n-1: Horizontal (X axis)\n-2: Vertical (Y axis)\n--> "))
            a=cls.choice
            if (a!=1 and a!=2): print("Invalid command\n")

    @classmethod
    def create_action(cls,position,db):
        if cls.choice==1: return Reflect_X(position, db)
        elif cls.choice==2: return Reflect_Y(position, db)
        
    @classmethod
    def params(cls):
        if cls.choice==1: return (f"Reflect; X")
        elif cls.choice==2: return (f"Reflect; Y")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        if commands[1]=="X":
            action = Reflect_X(position, dictionary.Dict["File"])
            dictionary.Change(("Reflect; X"), dictionary.Dict["File"][position], position)
        elif commands[1]=="Y":
            action = Reflect_Y(position, dictionary.Dict["File"])
            dictionary.Change(("Reflect; Y"), dictionary.Dict["File"][position], position)
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])