import questionary
from services.UserService import UserService;


class Home:
    def showMenuHome(self):
        while True:
            choice =  questionary.select(
            "O Que Você Deseja Acessar Hoje?",
            
                choices=[
                    'Filmes em Cartaz',
                    'Comprar Ingressos',
                    'Minhas Sessões',
                    'Sair'
                ],
                qmark="✮",
                
            ).ask();
        
            if choice == "Sair":
                question = questionary.select("Deseja Mesmo Sair?",choices=[
                    "Sim","Não"
                ], qmark="✮").ask();
                if question == "Sim":
                    from view.menu.PresententionMenu import PresentationMenu
                    presentation = PresentationMenu()
                    presentation.showPresentationMenu()
                    break;
                
    def showMenuHomeAdmin(self):
         while True:
            choice =  questionary.select(
            "O Que Você Deseja Acessar Hoje?",
            
                choices=[
                    'Filmes',
                    'Sessões',
                    'Salas',
                    "Sair"
                ],
                qmark="✮",
                
            ).ask();
           
            match choice:
                case  "Filmes":
                    return "Filmes page";
                case "Sessões":
                     return "Sessões page";
                case "Salas":
                     return "Salas page";
                case  "Sair":
                    question = questionary.select("Deseja Mesmo Sair?",choices=[
                        "Sim","Não"
                    ], qmark="✮").ask();
                    if question == "Sim":
                        from view.menu.PresententionMenu import PresentationMenu
                        presentation = PresentationMenu()
                        presentation.showPresentationMenu()
                        break;
                    