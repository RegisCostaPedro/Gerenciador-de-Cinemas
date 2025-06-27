import questionary
import time
from services.SessionService import SessionService;
from helpers import clearScream

class BuyTicketPage:
    def showBuyTicketPage(self):
       
        clearScream.Helpers.clearScreen()
        questionary.print("⋆⭒˚｡⋆ Sessões disponíveis ⋆⭒˚｡⋆\n\n")

        sessionsList = SessionService.getDisponibleSessionsJoin();

        if not sessionsList:
            questionary.print("Nenhuma sessão disponível...");
            print();
            questionary.confirm(message="←- Voltar",instruction=" (⏎)").ask();
            from view.menu.MenuHome import Home;
            home = Home();
            return home.showMenuHome();
         
        for session in sessionsList:
            print(f"Id: {session.get('id')}");
            print(f"Data: {session.get('date')}");
            print(f"Filme: {session.get('movie')}");
            print(f"Sala: {session.get('room')}");
            print();

        choices = [f"{session.get('id')} - {session.get('movie')} - {session.get('room')} - {session.get('date')}" for session in sessionsList];

        sessionSelected= questionary.select(message="", choices = choices).ask();

        sessionId = sessionSelected.split(' - ')[0];

        from helpers.persistUserId import getUserId;
        SessionService.addUserInSession(int(sessionId), getUserId());
        
        questionary.print(" ₊⊹ Ingresso comprado com sucesso! ₊⊹")
        time.sleep(1.5);
        questionary.print("Aguarde, redirecionando... ✮");

        from view.menu.MenuHome import Home;
        home = Home();
        return home.showMenuHome();