import questionary
from services.UserService import UserService;
from view.user_pages.userMoviePage import UserMoviePage
from view.user_pages.buyTicketPage import BuyTicketPage
from view.user_pages.userSessionsPage import UserSessionsPage
from view.admin_pages.moviePage import MoviePage
from view.admin_pages.roomPage import RoomPage
from view.admin_pages.sessionPage import SessionPage
from helpers import clearScream
from helpers.persistUserId import getUserId;

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

            movie = UserMoviePage();
            ticket = BuyTicketPage();
            sessions = UserSessionsPage();

            match choice:
                case  "Filmes em Cartaz":
                    return movie.showMoviePage();
                case "Comprar Ingressos":
                     return ticket.showBuyTicketPage();
                case "Minhas Sessões":
                     return sessions.showUserSessionsPage();
                case  "Sair":
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
            session = SessionPage();

            match choice:
                case  "Filmes":
                    return movie.showMoviePage();
                case "Sessões":
                     return session.showSessionPage();
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