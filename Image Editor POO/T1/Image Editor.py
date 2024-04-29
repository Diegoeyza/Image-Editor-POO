from Menu import Menu
from Database import Directory

directory=Directory()
menu=Menu()
menu.load_filters()
menu.load_compositions()
menu.Start(directory)