from view.PresententionMenu import PresentationMenu
from database.database import Database
from database.database import Roles
from database.database import connection

def main():
    presentationMenu = PresentationMenu()
    presentationMenu.showPresentationMenu()
    
if __name__ =="__main__":
    main()      