import questionary;
import time;
from services.SessionService import SessionService;
from helpers import clearScream;

class UserSessionsPage:
    def showUserSessionsPage(self):
       
        clearScream.Helpers.clearScreen()
        questionary.print("⋆⭒˚｡⋆ Suas sessões ⋆⭒˚｡⋆\n\n")

        from helpers.persistUserId import getUserId;
        sessionsList = SessionService.getUserSessions(getUserId());

        if not sessionsList:
            questionary.print("Você não possui nenhuma sessão...");
            print();
            questionary.confirm(message="←- Voltar",instruction=" (⏎)").ask();
            from view.menu.MenuHome import Home;
            home = Home();
            return home.showMenuHome();
         
        for session in sessionsList:
            print(f"Data: {session.get('date')}");
            print(f"Filme: {session.get('movie')}");
            print(f"Sala: {session.get('room')}");
            print(f"Ingressos: {session.get('tickets')}");
            print();

        print(".............................................................");
        questionary.confirm(message="←- Voltar",instruction=" (⏎)").ask()

        from view.menu.MenuHome import Home;
        home = Home();
        return home.showMenuHome();