from Filters import Negative
from Intermediary import FilterIntermediary
from typing import Optional

class InterNegative(FilterIntermediary):
    @classmethod
    def get_description(cls):
        return "Negative"

    @classmethod
    def ask_params(cls, position: Optional[int]=None, db: Optional[dict]=None):
        ...

    @classmethod
    def create_action(cls,position,db):
        return Negative(position, db)

    @classmethod
    def params(cls):
        return(f"Negative")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        action = Negative(position, dictionary.Dict["File"])
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])
        dictionary.Change("Negative", dictionary.Dict["File"][position], position)