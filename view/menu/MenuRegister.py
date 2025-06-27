import questionary
import time;
from services.UserService import UserService;
from database.database import connection,Database
from view.menu.MenuHome import Home

class MenuRegister:
    def showMenu(self):
        
        userData = questionary.form(
            login=questionary.text("Nome: "),
            password=questionary.password("Senha: ")
        ).ask()
        
        UserService.registerUser(userData);
        userRegistred = UserService.authenticateUser(userData);

        from helpers.persistUserId import setUserId;
        setUserId(userRegistred.get('id'));

        if userRegistred:
            questionary.confirm(message="",auto_enter=True)
            home = Home()
            home.showMenuHome();
            
