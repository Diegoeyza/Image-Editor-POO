from Filters import Highlight
from Intermediary import FilterIntermediary
from typing import Optional

class InterHighlight(FilterIntermediary):
    @classmethod
    def get_description(cls):
        return "Highlight"

    @classmethod
    def ask_params(cls, position: Optional[int]=None, db: Optional[dict]=None):
        cls.ValueR = int(input("Insert R (0-255): "))
        cls.ValueG = int(input("Insert G (0-255): "))
        cls.ValueB = int(input("Insert B (0-255): "))
        cls.Tolerance = int(input("Insert a tolerance (0-255): "))

    @classmethod
    def create_action(cls,position,db):
        return Highlight(position, db, cls.ValueR, cls.ValueG, cls.ValueB, cls.Tolerance)

    @classmethod
    def params(cls):
        return(f"Highlight; {cls.ValueR}; {cls.ValueG}; {cls.ValueB}; {cls.Tolerance}")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        action = Highlight(position, dictionary.Dict["File"], int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]))
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])
        dictionary.Change(f"Highlight; {commands[1]}; {commands[2]}; {commands[3]}; {commands[4]}", dictionary.Dict["File"][position], position)