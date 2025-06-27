import questionary;
from services.UserService import UserService;
from database.database import connection,Database;
from view.menu.MenuHome import Home


class MenuLogin:
    def showMenu(self):
          while True:
            userAuth = questionary.form(
                login=questionary.text("Nome: "),
                password=questionary.password("Senha: ")
            ).ask();

            userAuthenticated = UserService.authenticateUser(userAuth);
          
            if userAuthenticated is not None and userAuthenticated is not False:
                    home = Home();
                    UserIsAdmin = UserService.checkIfUserIsAdmin(userAuthenticated);
                
                    match UserIsAdmin:
                        case True:
                            return home.showMenuHomeAdmin();
                        case False:
                            return home.showMenuHome()
                    break; 
            else:
              questionary.print("Usuário ou senha incorretos", style="bold fg:red");