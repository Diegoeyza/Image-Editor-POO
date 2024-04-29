from Intermediary.Composition_Intermediary import CompIntermediary
from Database import FileCheck
from typing import Optional
from Compositions import Paste_Right, Paste_Left, Paste_Over, Paste_Below

class InterPaste(CompIntermediary):
    @classmethod
    def get_description(cls):
        return ("Paste two images")

    @classmethod
    def ask_params(cls, position: Optional[int], db: Optional[dict]):
        cls.filename2 = FileCheck(input("Insert path for the second image:\n--> "))
        cls.choice=0
        while (cls.choice!=1 and cls.choice!=2 and cls.choice!=3 and cls.choice!=4):
            cls.choice = int(input("- Select 1 to paste to the right\n- Select 2 to paste to the left\n- Select 3 to paste on top\n- Select 4 to paste below\n--> "))
            if (cls.choice!=1 and cls.choice!=2 and cls.choice!=3 and cls.choice!=4): print("Invalid entry")

    @classmethod
    def create_action(cls, position, db):
        if cls.choice == 1:
            return Paste_Right(position, db, cls.filename2)
        elif cls.choice == 2:
            return Paste_Left(position, db, cls.filename2)
        elif cls.choice == 3:
            return Paste_Over(position, db, cls.filename2)
        elif cls.choice == 4:
            return Paste_Below(position, db, cls.filename2)
    
    @classmethod
    def params(cls):
        if cls.choice == 1:
            return (f"Paste two images; Right; {cls.filename2}")
        elif cls.choice == 2:
            return (f"Paste two images; Left; {cls.filename2}")
        elif cls.choice == 3:
            return (f"Paste two images; Over; {cls.filename2}")
        elif cls.choice ==4:
            return (f"Paste two images; Below; {cls.filename2}")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        if commands[1]=="Right":
            action = Paste_Right(position, dictionary.Dict["File"], commands[2])
            dictionary.Change((f"Paste two images; Right; {commands[2]}"), dictionary.Dict["File"][position], position)
        elif commands[1]=="Left":
            action = Paste_Left(position, dictionary.Dict["File"], commands[2])
            dictionary.Change((f"Paste two images; Left; {commands[2]}"), dictionary.Dict["File"][position], position)
        elif commands[1]=="Over":
            action = Paste_Over(position, dictionary.Dict["File"], commands[2])
            dictionary.Change((f"Paste two images; Over; {commands[2]}"), dictionary.Dict["File"][position], position)
        elif commands[1]=="Below":
            action = Paste_Below(position, dictionary.Dict["File"], commands[2])
            dictionary.Change((f"Paste two images; Below; {commands[2]}"), dictionary.Dict["File"][position], position)
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])