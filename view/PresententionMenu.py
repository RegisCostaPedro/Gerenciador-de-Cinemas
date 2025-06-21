import questionary;
from view.MenuLogin import MenuLogin
from view.MenuRegister import MenuRegister

class PresentationMenu:
    def showPresentationMenu(self):
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
            return menu.showMenu();        
        elif authMethod == "Cadastro":
            menu = MenuRegister();
            menu.showMenu();