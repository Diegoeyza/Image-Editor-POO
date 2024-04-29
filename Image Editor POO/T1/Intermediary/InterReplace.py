from Filters import Replace
from Intermediary import FilterIntermediary
from typing import Optional

class InterReplace(FilterIntermediary):
    @classmethod
    def get_description(cls):
        return("Replace")

    @classmethod
    def ask_params(cls, position: Optional[int], db: Optional[dict]):
        cls.r1 = int(input("R value of color to replace (0-255):\n>"))
        cls.g1 = int(input("G value of color to replace (0-255):\n>"))
        cls.b1 = int(input("B value of color to replace (0-255):\n>"))
        cls.tolerance = int(input("Tolerance (0-255):\n>"))
        cls.r2 = int(input("R value of replacing color (0-255):\n>"))
        cls.g2 = int(input("G value of replacing color (0-255):\n>"))
        cls.b2 = int(input("B value of replacing color (0-255):\n>"))

    @classmethod
    def create_action(cls, position, db):
        return Replace(position, db, cls.r1, cls.g1, cls.b1, cls.tolerance, cls.r2, cls.g2, cls.b2)
    
    @classmethod
    def params(cls):
        return(f"Replace; {cls.r1}; {cls.g1}; {cls.b1}; {cls.tolerance}; {cls.r2}; {cls.g2}; {cls.b2}")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        action = Replace(position, dictionary.Dict["File"], int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]), int(commands[5]), int(commands[6]), int(commands[7]))
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])
        dictionary.Change(f"Replace; {commands[1]}; {commands[2]}; {commands[3]}; {commands[4]}; {commands[5]}; {commands[6]}; {commands[7]}", dictionary.Dict["File"][position], position)