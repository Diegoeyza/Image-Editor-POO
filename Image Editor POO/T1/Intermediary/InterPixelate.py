from Filters import Pixelate
from Intermediary import FilterIntermediary
from typing import Optional

class InterPixelate(FilterIntermediary):
    @classmethod
    def get_description(cls):
        return "Pixelate"

    @classmethod
    def ask_params(cls, position: Optional[int]=None, db: Optional[dict]=None):
        cls.Pxl =int(input("Insert pixel amount\n--> "))

    @classmethod
    def create_action(cls,position,db):
        return Pixelate(position, db, cls.Pxl)

    @classmethod
    def params(cls):
        return(f"Pixelate; {cls.Pxl}")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        action = Pixelate(position, dictionary.Dict["File"], int(commands[1]))
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])
        dictionary.Change(f"Pixelate; {commands[1]}", dictionary.Dict["File"][position], position)
