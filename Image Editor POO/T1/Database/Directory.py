import json
from Database import JsonCheck
from PIL import Image

class Directory:
    def __init__(self):
        self.Dict={"Project":[],"File":[],"Changes":[],"Checkpoint":[],"Scripts":[]}
        self.position=0


    def New_project(self, name, file, original_file):
        (self.Dict["Project"]).append(name)
        (self.Dict["File"]).append(file)
        (self.Dict["Checkpoint"]).append(original_file)
        (self.Dict["Changes"]).append("Base Image/")
        (self.Dict["Scripts"]).append("None/")
    

    def Change(self, change, file, position):
        (self.Dict["File"])[position]=file
        (self.Dict["Changes"])[position]+=f"{change}/"

    def Empty_changes(self, position):
        (self.Dict["Changes"][position])="Base Image/"
    
    def Empty_scripts(self, position):
        (self.Dict["Scripts"][position])="None/"

    def changelog(self,position):
        changes=(self.Dict["Changes"][position]).split("/")
        if (len(changes)<3):
            print("There haven't been any changes yet")
            return None
        print(f"The changelog of {self.Dict['File'][position]} is:")
        if len(self.Dict["Scripts"][position])>5:
            scripts=self.Dict["Scripts"][position].split("/")
            for i in range (0,len(changes)-1):
                print(f"{i}-{changes[i]}")
            print(f"\nThe scripts applied to {self.Dict['File'][position]} are:")
            for i in range (1,len(scripts)-1):
                info=scripts[i].split("; ")
                print(f"{i}-{info[0]}: including changes {int(info[2])} to {int(info[2])-1+int(info[1])}")
        else:
            for i in range (0,len(changes)-1):
                print(f"{i}-{changes[i]}")

    def Save_file(self, Project_position):
        Im = Image.open(self.Dict["File"][Project_position]).convert('RGB')
        Im.save(f'Saved_{self.Dict["File"][Project_position]}')
        Im.close()
        Saved_dict = {"Project": self.Dict["Project"][Project_position], "File": f'Saved_{self.Dict["File"][Project_position]}',"Changes": self.Dict["Changes"][Project_position],"Checkpoint": self.Dict["Checkpoint"][Project_position],"Scripts": self.Dict["Scripts"][Project_position]}
        with open(f"Saved_{Saved_dict['Project']}","w") as sf:
            json.dump(Saved_dict, sf)
        print("Save successful")
    
    def Save_script(self, Project_position):
        name=input("Please give a name to the script: ")
        Saved_script = {"Name": name, "Commands": f'{self.Dict["Changes"][Project_position]}'}
        with open(f"Script_{name}","w") as sf:
            json.dump(Saved_script, sf)
        print("Save successful")
    
    def Open_script(self,Saved_script):
        with open(Saved_script, "r") as lf:
            New_script = json.load(lf)
        print("Load successful")
        return New_script

    
    def Open_file(self, Saved_dict):
        with open(Saved_dict, "r") as lf:
            New_dict = json.load(lf)
        (self.Dict["Project"]).append(New_dict["Project"])
        (self.Dict["File"]).append(New_dict["File"])
        (self.Dict["Checkpoint"]).append(New_dict["Checkpoint"])
        (self.Dict["Changes"]).append(New_dict["Changes"])
        (self.Dict["Scripts"]).append(New_dict["Scripts"])
        print("Load successful")

    def _print(self):
        print(self.Dict)
    
    def decode(self):
        file = JsonCheck(input("Please select the path of the script to load: "))
        script=self.Open_script(file)
        while(True):
            entry=input(f'Do you want to use the script {script["Name"]} (Y/N) (Enter info to display what is inside of the script)\n')
            self.script_name=script["Name"]
            changes=script["Commands"].split("/")
            if entry=="Y" or entry=="y":
                return changes
            elif entry=="info" or entry=="INFO":
                print("\nThe commands inside of the script are: ")
                for i in range (1, len(changes)-1):
                    print(f"{i}-{changes[i]}")
            else: return 0
    
    def ScriptAdd(self, changes, position): (self.Dict["Scripts"][position])+=f'{self.script_name}; {len(changes)-2}; {self.Dict["Changes"][position].count("/")}/'
    
    def ScriptLoad(self, line, filters, compositions):
        for i in range (0,len(filters)):
            if (filters[i]).get_description()==line[0]:
                return filters[i]
        for i in range (0,len(compositions)):
            if (compositions[i]).get_description()==line[0]:
                return compositions[i]
        return None
            