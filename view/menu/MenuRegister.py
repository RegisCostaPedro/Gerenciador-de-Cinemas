import questionary
from services.UserService import UserService;
from database.database import connection,Database
from view.menu.MenuHome import Home
class MenuRegister:
    def showMenu(self):
        userData = questionary.form(
            login=questionary.text("Nome: "),
            password=questionary.password("Senha: ")
        ).ask()
        
        userRegistred = UserService.registerUser(userData)
        if userRegistred:
            home = Home()
            home.showMenuHome();
            
