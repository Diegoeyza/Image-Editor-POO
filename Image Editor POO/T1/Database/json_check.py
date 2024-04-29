import json

def JsonCheck(file):
    Check = 0
    while Check != 1:
        try:
            with open(file, "r"):
                ...

        except IOError:
             print("No such file or directory, try again")
             file = input("Insert file path:\n")
        else:
            Check = 1
            return file