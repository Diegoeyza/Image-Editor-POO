from Filters import Resize
from PIL import Image
from Intermediary import FilterIntermediary

class InterResize(FilterIntermediary):
    @classmethod
    def get_description(cls):
        return "Resize" 

    @classmethod
    def ask_params(cls, position, db):
        Img=Image.open(db[position]).convert('RGB')
        print(f"Current image size is {Img.width}x{Img.height}")
        print("Select the new size")
        cls.width = int(input("Width: "))
        cls.height = int(input("Height: "))

    @classmethod
    def create_action(cls,position,db):
        return Resize(position, db, cls.width, cls.height)

    @classmethod
    def params(cls):
        return(f"Resize; {cls.width}; {cls.height}")
    
    @classmethod
    def ScriptAction(cls, dictionary, position, commands):
        action = Resize(position, dictionary.Dict["File"], int(commands[1]), int(commands[2]))
        cls.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][position])
        dictionary.Change(f"Resize; {commands[1]}; {commands[2]}", dictionary.Dict["File"][position], position)