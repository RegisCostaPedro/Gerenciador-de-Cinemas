import questionary
from services.UserService import UserService;
from database.database import connection,Database
class MenuLogin:
    def showMenu(self):
        userAuth = questionary.form(
            
            name=questionary.text("Nome: "),
            password=questionary.password("Senha: ")
        ).ask()
        
        UserService.authenticateUser(userAuth)
      
