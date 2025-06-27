import questionary;
from view.menu.MenuLogin import MenuLogin
from view.menu.MenuRegister import MenuRegister
from helpers import clearScream
class PresentationMenu:
    def showPresentationMenu(self):
        clearScream.Helpers.clearScreen()
        questionary.print(f"─ ⊹ ⊱ CINE ˗ˏˋ ★ ˎˊ˗ BIGOR  ⊰ ⊹ ─",style="blink fg:#fff bg:black bold")


        questionary.text("Cadastrar/Login")

        authMethod =  questionary.select(
           
            "Selecione Login ou Cadastro",
            choices=[
                'Login',
                'Cadastro'
            ],
             qmark="✮",
        ).ask()
        
    
        if authMethod == "Login":
            menu = MenuLogin();
            questionary.confirm(message="",auto_enter=True)
            return menu.showMenu();        
        elif authMethod == "Cadastro":
            menu = MenuRegister();
            menu.showMenu();