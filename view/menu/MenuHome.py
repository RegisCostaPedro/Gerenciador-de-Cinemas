import questionary
from services.UserService import UserService;
from view.admin_pages.moviePage import MoviePage
from view.admin_pages.roomPage import RoomPage
from helpers import clearScream

class Home:
    def showMenuHome(self):
        while True:
            
            clearScream.Helpers.clearScreen()
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
         clearScream.Helpers.clearScreen()
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
            movie = MoviePage();
            room = RoomPage();
            match choice:
                case  "Filmes":
                    return movie.showMoviePage();
                case "Sessões":
                     return "Sessões page";
                case "Salas":
                     return room.showRoomPage();
                case  "Sair":
                    question = questionary.select("Deseja Mesmo Sair?",choices=[
                        "Sim","Não"
                    ], qmark="✮").ask();
                    if question == "Sim":
                        from view.menu.PresententionMenu import PresentationMenu
                        presentation = PresentationMenu()
                        presentation.showPresentationMenu()
                        break;
                    