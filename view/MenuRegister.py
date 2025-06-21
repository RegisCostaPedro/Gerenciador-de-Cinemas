import questionary
from services.UserService import UserService;
from database.database import connection,Database
from view.MenuHome import Home
class MenuRegister:
    def showMenu(self):
        userData = questionary.form(
            name=questionary.text("Nome: "),
            password=questionary.password("Senha: ")
        ).ask()
        
        userRegistred = UserService.registerUser(userData)
        if userRegistred:
            home = Home()
            home.showMenuHome();
            
