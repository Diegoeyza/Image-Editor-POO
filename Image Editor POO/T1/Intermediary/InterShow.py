from PIL import Image

def Image_Show(position,db):
    Image.open(db[position]).convert('RGB').show()