from Intermediary.Composition_Intermediary import CompIntermediary
from Database import FileCheck
from typing import Optional
from Compositions import Watermark

class InterWatermark(CompIntermediary):
    @classmethod
    def get_description(cls):
        return ("Watermark")

    @classmethod
    def ask_params(cls, position: Optional[int], db: Optional[dict]):
        cls.filename2 = FileCheck(input("Insert path for the second image:\n--> "))

    @classmethod
    def create_action(cls, position, db):
        return Watermark(position, db, cls.filename2)

    @classmethod
    def params(cls):
        return (f"Watermark; {cls.filename2}")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        action = Watermark(position, dictionary.Dict["File"], commands[1])
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])
        dictionary.Change(f"Watermark; {commands[1]}", dictionary.Dict["File"][position], position)