from Filters import GrayScale
from Intermediary import FilterIntermediary
from typing import Optional

class InterGrayscale(FilterIntermediary):
    @classmethod
    def get_description(cls):
        return "Grayscale"

    @classmethod
    def ask_params(cls, position: Optional[int]=None, db: Optional[dict]=None):
        ...

    @classmethod
    def create_action(cls,position,db):
        return GrayScale(position, db)

    @classmethod
    def params(cls):
        return(f"Grayscale")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        action = GrayScale(position, dictionary.Dict["File"])
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])
        dictionary.Change("Grayscale", dictionary.Dict["File"][position], position)