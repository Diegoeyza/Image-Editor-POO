from PIL import Image
import Intermediary
from Filters import*
from Compositions import*
from Database import FileCheck, JsonCheck
from Intermediary import*


class Menu():
    def __init__(self):
        self.exit="0"
        self.entry=""
    
    def load_filters(self):
        self.filter_list=[cls_obj for cls_name, cls_obj in vars(Intermediary).items() if isinstance(cls_obj, type) and issubclass(cls_obj, Intermediary.FilterIntermediary) and cls_obj is not Intermediary.FilterIntermediary]

    def load_compositions(self):
        self.comp_list=[cls_obj for cls_name, cls_obj in vars(Intermediary).items() if isinstance(cls_obj, type) and issubclass(cls_obj, Intermediary.CompIntermediary) and cls_obj is not Intermediary.CompIntermediary]
    
    def show_filters(self):
        for i in range (0,len(self.filter_list)):
            print(f"{i+1}-{(self.filter_list[i]).get_description()}")
        print(f"{len(self.filter_list)+1}-To go back")
        return int(input("Select a filter to apply by entering its index:\n--> "))
    
    def show_comp(self):
        for i in range (0,len(self.comp_list)):
            print(f"{i+1}-{(self.comp_list[i]).get_description()}")
        print(f"{len(self.comp_list)+1}-To go back")
        return int(input("Select a composition to apply by entering its index:\n--> "))
    
    def _executeFilter(self, option_idx, dictionary):
        item = self.filter_list[option_idx-1]
        item.ask_params(self.position,dictionary.Dict["File"])
        action = item.create_action(self.position,dictionary.Dict["File"])
        self.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][self.position])
        dictionary.Change(item.params(), dictionary.Dict["File"][self.position], self.position)
        Image_Show(self.position, dictionary.Dict["File"])
    
    def _executeComp(self, option_idx, dictionary):
        item = self.comp_list[option_idx-1]
        item.ask_params(self.position,dictionary.Dict["File"])
        action = item.create_action(self.position,dictionary.Dict["File"])
        self.editIM = action.Apply()
        action.Img.save(dictionary.Dict["File"][self.position])
        dictionary.Change(item.params(), dictionary.Dict["File"][self.position], self.position)
        Image_Show(self.position, dictionary.Dict["File"])

    def undo(self, dictionary):
        self.changes=(dictionary.Dict["Changes"][self.position]).split("/")
        if (len(self.changes)<3):
            print("There haven't been any changes yet")
            return None
        print(f"The changes made to {dictionary.Dict['File'][self.position]} are:")
        if len(dictionary.Dict["Scripts"][self.position])>5:
            print(len(dictionary.Dict["Scripts"][self.position]))
            scripts=dictionary.Dict["Scripts"][self.position].split("/")
            for i in range (0,len(self.changes)-1):
                print(f"{i}-{self.changes[i]}")
            print(f"\nThe scripts applied to {dictionary.Dict['File'][self.position]} are:")
            for i in range (1,len(scripts)-1):
                info=scripts[i].split("; ")
                print(f"{i}-{info[0]}-->To undo enter {int(info[2])-1}")
            
            self.load=input("Please select the index number of a change to undo all of the changes up to that point or type BACK to return to the menu:\n--> ")
            if (self.load=="BACK" or self.load=="back" or self.load=="Back"):
                ...
            elif (self.load)=="0":
                Im = Image.open(dictionary.Dict["Checkpoint"][self.position]).convert('RGB')
                Im.save(dictionary.Dict["File"][self.position])
                dictionary.Empty_changes(self.position)
                dictionary.Empty_scripts(self.position)

            elif (int(self.load)>0 and int(self.load)<len(self.changes)):  
                Im = Image.open(dictionary.Dict["Checkpoint"][self.position]).convert('RGB')
                Im.save(dictionary.Dict["File"][self.position])   
                dictionary.Empty_changes(self.position)
                if int(self.load)<int((scripts[1].split("; "))[2]):
                    dictionary.Empty_scripts(self.position)
                for i in range (1, int(self.load)+1):
                    commands=self.changes[i].split("; ")
                    item=dictionary.ScriptLoad(commands, self.filter_list, self.comp_list)
                    item.ScriptAction(dictionary, self.position, commands)
            else: return None
            Image_Show(self.position, dictionary.Dict["File"])
                

        else:
            for i in range (0,len(self.changes)-1):
                print(f"{i}-{self.changes[i]}")
            self.load=input("Please select the index number of a change to undo all of the changes up to that point or type BACK to return to the menu:\n--> ")
            if (self.load=="BACK" or self.load=="back" or self.load=="Back"):
                ...
            elif (self.load)=="0":
                Im = Image.open(dictionary.Dict["Checkpoint"][self.position]).convert('RGB')
                Im.save(dictionary.Dict["File"][self.position])
                dictionary.Empty_changes(self.position)

            elif (int(self.load)>0 and int(self.load)<len(self.changes)):  
                Im = Image.open(dictionary.Dict["Checkpoint"][self.position]).convert('RGB')
                Im.save(dictionary.Dict["File"][self.position])   
                dictionary.Empty_changes(self.position)   
                for i in range (1, int(self.load)+1):
                    commands=self.changes[i].split("; ")
                    item=dictionary.ScriptLoad(commands, self.filter_list, self.comp_list)
                    item.ScriptAction(dictionary, self.position, commands)
            else: return None
            Image_Show(self.position, dictionary.Dict["File"])


    def _decoder(self,dictionary):
        script=dictionary.decode()
        exit=0
        if script!=0:
            print("The projects where you can apply a script are:")
            for i in range (0, len(dictionary.Dict["Project"])):
                print(f"-{i+1}: ",end="")
                print(dictionary.Dict["Project"][i]+" --> "+dictionary.Dict["File"][i])
            self.position=int(input("Please select the project that you wish to modify: "))-1
            dictionary.ScriptAdd(script, self.position)
            for i in range (1, len(script)-1):
                commands=script[i].split("; ")
                item=dictionary.ScriptLoad(commands, self.filter_list, self.comp_list)
                if item!=None:
                    item.ScriptAction(dictionary, self.position, commands)
                else: exit=1
            if exit==0:
                Image_Show(self.position, dictionary.Dict["File"])
            else: print("The script has an invalid filter or composition")

    
    def Start(self,dictionary):
        while(self.exit=="0"):
            self.entry=input(f"\nWelcome to Pillow Image editor, please select one of the following commands by entering its index:\n1-Start a new project\n2-Work on an existing project\n3-Show an image from a project\n4-Show the changes on a project\n5-Undo changes on a project\n6-Save a project\n7-Load a previously saved project\n8-Save a script\n9-Load a script\n\nTo close the editor, type END\n")
            if (self.entry=="END" or self.entry=="End" or self.entry=="end"):
                self.exit=1
            
            elif (self.entry=="1"):
                self.pexit=0
                self.position=0
                pname=input("Please enter the name you will give to your new project (it must be unique): ")
                self.pfile=FileCheck(input("Please enter the path of the picture you want to edit: "))
                Im = Image.open(self.pfile).convert('RGB')
                Im.save(f'{pname}_Base_{self.pfile}')
                Im.save(f'{pname}_Edited_{self.pfile}')
                dictionary.New_project(pname, f'{pname}_Edited_{self.pfile}', f'{pname}_Base_{self.pfile}')
                self.position=dictionary.Dict["Project"].index(pname)
            
            elif (self.entry=="2"):
                if (len(dictionary.Dict["Project"])==0):
                    print("There are no projects available, please create a new one at the menu\n")
                    continue
                elif (len(dictionary.Dict["Project"])!=0):
                    self.position=0
                    self.pexit=0
                    print("\nThe projects that are available are: ")
                    for i in range (0, len(dictionary.Dict["Project"])):
                        print(f"-{i+1}: ",end="")
                        print(dictionary.Dict["Project"][i]+" --> "+dictionary.Dict["File"][i])
                    self.position=int(input("Please select a project to open by entering its index number: "))-1
            
            elif (self.entry=="3"):
                if (len(dictionary.Dict["Project"])==0):
                    print("There are no projects yet\n")
                    continue
                elif (len(dictionary.Dict["Project"])!=0):
                        self.position=0
                        self.pexit=0
                        print("\nThe projects that are available are: ")
                        for i in range (0, len(dictionary.Dict["Project"])):
                            print(f"-{i+1}: ",end="")
                            print(dictionary.Dict["Project"][i]+" --> "+dictionary.Dict["File"][i])
                        self.position=int(input("Please select a project to show by entering its index number: "))-1
                        print("Loading image...")
                        Image_Show(self.position,dictionary.Dict["File"])

            elif (self.entry=="4"):
                if (len(dictionary.Dict["Project"])==0):
                    print("There are no projects available\n")
                    continue
                
                elif (len(dictionary.Dict["Project"])!=0):
                    self.position=0
                    self.pexit=0
                    print("\nThe projects that are available are: ")
                    for i in range (0, len(dictionary.Dict["Project"])):
                        print(f"-{i+1}: ",end="")
                        print(dictionary.Dict["Project"][i]+" --> "+dictionary.Dict["File"][i])
                    self.position=int(input("Please select a project to check its changelog by selecting its index number: "))-1
                    dictionary.changelog(self.position)
            
            elif (self.entry=="5"):
                if (len(dictionary.Dict["Project"])==0):
                    print("There are no projects available\n")
                    continue
                elif (len(dictionary.Dict["Project"])!=0):
                    self.position=0
                    print("\nThe projects that are available are: ")
                    for i in range (0, len(dictionary.Dict["Project"])):
                        print(f"-{i+1}: ",end="")
                        print(dictionary.Dict["Project"][i]+" --> "+dictionary.Dict["File"][i])
                    self.position=int(input("Please select the project that you wish to modify: "))-1
                    if self.position>=0 and self.position<(len(dictionary.Dict["Project"])):
                        self.undo(dictionary)
                    else: print("Index out of range, returning to the menu...")
            
            elif(self.entry=="6"):
                if (len(dictionary.Dict["Project"])==0):
                    print("There are no projects yet\n")
                    continue
                else:
                    print("\nThe projects that can be saved are: ")
                    for i in range (0, len(dictionary.Dict["Project"])):
                        print(f"-{i+1}: ",end="")
                        print(dictionary.Dict["Project"][i]+" --> "+dictionary.Dict["File"][i])
                    Project_position = int(input("Please select a project to save by entering its index number: "))-1
                    if Project_position>=0 and Project_position<(len(dictionary.Dict["Project"])):
                        dictionary.Save_file(Project_position)
                    else: print("Index out of range, returning to the menu...")

            elif(self.entry=="7"):
                File_to_load = JsonCheck(input("Please select the path of the project to load: "))
                dictionary.Open_file(File_to_load)
            
            elif(self.entry=="8"):
                if (len(dictionary.Dict["Project"])==0):
                    print("There are no projects yet\n")
                    continue
                else:
                    print("\nThe scripts from projects that can be saved are: ")
                    for i in range (0, len(dictionary.Dict["Project"])):
                        print(f"-{i+1}: ",end="")
                        print(dictionary.Dict["Project"][i]+" --> "+dictionary.Dict["File"][i])
                    Project_position = int(input("Please select a script to save by entering its index number: "))-1
                    if Project_position>=0 and Project_position<(len(dictionary.Dict["Project"])):
                        dictionary.Save_script(Project_position)
                    else: print("Index out of range, returning to the menu...")
            
            elif(self.entry=="9"):
                if (len(dictionary.Dict["Project"])==0):
                    print("There are no projects yet\n")
                    continue
                else:
                    self._decoder(dictionary)
            
            if ((self.entry=="1"or self.entry=="2") and 0<=self.position<len(dictionary.Dict["Project"])):
                while (self.pexit==0):
                    efile=dictionary.Dict["File"][self.position]
                    choice = int(input(f"\nPlease select what do you want to do to {efile}\n-1 Filters\n-2 Compositions:\n-3 Go back\n--> "))
                    if(choice == 1):
                        self.edit = self.show_filters()
                        if (self.edit > len(self.filter_list) or self.edit <= 0):
                            continue
                        self._executeFilter(self.edit,dictionary)
                    elif(choice == 2):
                        self.edit = self.show_comp()
                        if (self.edit > len(self.comp_list) or self.edit <= 0):
                            continue
                        self._executeComp(self.edit,dictionary)
                    elif(choice == 3):
                        self.pexit = 1
                    else:
                        continue
