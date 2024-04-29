from PIL import Image

def FileCheck(file):
    Check = 0
    while Check != 1:
        try:
            Opened = Image.open(file).convert('RGB')
            Opened.close()
        except IOError:
             print("No such file or directory, try again")
             file = input("Insert image path:\n")
        else:
            Check = 1
            return file