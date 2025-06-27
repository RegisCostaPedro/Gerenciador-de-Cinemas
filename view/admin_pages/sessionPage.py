from typing import Any;

import questionary;
import questionary.question;
import time;
from services.SessionService import SessionService;
from services.RoomService import RoomService;
from services.MovieService import MovieService;
from database.database import connection, Database;
from helpers import clearScream;
     
class SessionPage:

    def showSessionPage(self):
        clearScream.Helpers.clearScreen();
        questionary.print(f" ˗ˏˋ Sessões ⊹ ─                                ", style="blink fg:#fff bg:black bold")

        choices = [ 'Adicionar Sessão', 'Listar Sessões', 'Atualizar Sessão', 'Remover Sessão', 'Voltar' ];
        sessionChoice = questionary.select(" ", choices=choices, qmark="✮").ask();

        match sessionChoice:
            case "Adicionar Sessão":
                return self.showRegisterSessionPage();
            case "Listar Sessões":
                return self.showListSessionsPage();
            case 'Atualizar Sessão':
                return self.showUpdateSessionPage()
            case 'Remover Sessão':
                return self.showRemoveSessionPage()
            case 'Voltar':
                from view.menu.MenuHome import Home;
                home = Home();
                home.showMenuHomeAdmin();
                
    def showListSessionsPage(self):
        clearScream.Helpers.clearScreen(); 
        questionary.print("⋆⭒˚｡⋆ Sessões ⋆⭒˚｡⋆\n\n");

        sessionList = SessionService.getSessionsJoin();

        if sessionList:
           for session in sessionList:
            print(f"Id: {session.get('id')}");
            print(f"Data: {session.get('date')}");
            print(f"Filme: {session.get('movie')}");
            print(f"Sala: {session.get('room')}");
            print();
        else:
            print("Nenhuma sessão registrada...");

        print(".............................................................")

        questionary.confirm(message="←- Voltar", instruction=" (⏎)").ask();
        return self.showSessionPage();
    
    def showRegisterSessionPage(self):
        clearScream.Helpers.clearScreen();
        questionary.print("Digite as Informações da Sessão");

        roomList = RoomService.getRooms();
        movieList = MovieService.getMovies();

        sessionObj = questionary.form(
            date = questionary.text("Informe a data da sessão: "),
        ).ask();

        if not roomList:
            questionary.print("Não há salas registradas, não é possível registrar uma sessão...");
            print();
            questionary.confirm(message="←- Voltar", instruction=" (⏎)").ask();
            return self.showSessionPage();

        if not movieList:
            questionary.print("Não há filmes registrados, não é possível registrar uma sessão...");
            print();
            questionary.confirm(message="←- Voltar", instruction=" (⏎)").ask();
            return self.showSessionPage();
         
        roomChoices = [f"{room.get('id')} - {room.get('name')}" for room in roomList];
        movieList = [f"{movie.get('id')} - {movie.get('name')}" for movie in movieList];

        print();
        questionary.print("Escolha uma sala para a sessão: ");
        roomSelected= questionary.select(message="", choices=roomChoices).ask();

        print();
        questionary.print("Escolha um filme para a sessão: ");
        movieSelected= questionary.select(message="", choices=movieList).ask();

        idMovie = roomSelected.split(' - ')[0];
        idRoom = roomSelected.split(' - ')[0];

        sessionObj['movie_id'] = int(idMovie);
        sessionObj['room_id'] = int(idRoom);
        sessionObj['users'] = [];

        SessionService.registerSession(sessionObj);

        questionary.print("✮ Sessão salva com sucesso! ✮");
        questionary.print("Aguarde, redirecionando... ✮");
        time.sleep(1.5);
        self.showSessionPage();

    def showRemoveSessionPage(self):
        clearScream.Helpers.clearScreen();

        questionary.print("⋆⭒˚｡⋆ Sessões ⋆⭒˚｡⋆\n\n");
        print();
        questionary.print("Selecione uma sessão para excluir");
        print();
       
        sessionsList = SessionService.getSessionsJoin();

        if not sessionsList:
             questionary.print("Nenhuma sessão registrada...");
             print();
             questionary.confirm(message="←- Voltar", instruction=" (⏎)").ask();
             return self.showSessionPage();
         
        choices = [f"{session.get('id')} - {session.get('movie')} - {session.get('room')} - {session.get('date')}" for session in sessionsList];

        sessionSelected= questionary.select(message="", choices = choices).ask();
       
        print(".............................................................")
        
        idToDelete= sessionSelected.split(' - ')[0];

        sessionDeleted = SessionService.deleteSession(int(idToDelete));
        
        if sessionDeleted:
            questionary.print(" ✖ Sessão removida!");
            time.sleep(1.5);
            questionary.print("Aguarde, redirecionando... ✮");
            return self.showSessionPage();
        
    def showUpdateSessionPage(self):
        clearScream.Helpers.clearScreen();
        questionary.print("⋆⭒˚｡⋆ Sals ⋆⭒˚｡⋆\n\n");
        questionary.print("Selecione uma sala para editar");
       
        sessionsList = SessionService.getSessionsJoin();

        if not sessionsList:
             questionary.print("Nenhuma sessão registrada...");
             print();
             questionary.confirm(message="←- Voltar",instruction=" (⏎)").ask();
             return self.showRoomPage();
         
        for session in sessionsList:
            print(f"Id: {session.get('id')}");
            print(f"Data: {session.get('date')}");
            print(f"Filme: {session.get('movie')}");
            print(f"Sala: {session.get('room')}");
            print();

        choices = [f"{session.get('id')} - {session.get('movie')} - {session.get('room')} - {session.get('date')}" for session in sessionsList];

        sessionSelected= questionary.select(message="", choices = choices).ask();
       
        print();
        print("⋆.˚ ──────────────────────── Atualize as Informações da Sessão ─────────────────────── ⋆.˚\n")
        
        roomList = RoomService.getRooms();
        movieList = MovieService.getMovies();

        roomChoices = [f"{room.get('id')} - {room.get('name')}" for room in roomList];
        movieList = [f"{movie.get('id')} - {movie.get('name')}" for movie in movieList];

        newSessionObj = questionary.form(
            date = questionary.text("Informe a data da sessão: "),
        ).ask();

        print();
        questionary.print("Escolha uma sala para a sessão: ");
        roomSelected= questionary.select(message="", choices=roomChoices).ask();

        print();
        questionary.print("Escolha um filme para a sessão: ");
        movieSelected= questionary.select(message="", choices=movieList).ask();

        idMovie = roomSelected.split(' - ')[0];
        idRoom = roomSelected.split(' - ')[0];

        newSessionObj['movie_id'] = int(idMovie);
        newSessionObj['room_id'] = int(idRoom);

        idToUpdate= sessionSelected.split(' - ')[0];
        sessionUpdated = SessionService.updateSession(int(idToUpdate), newSessionObj);
        
        if sessionUpdated:
            questionary.print(" ₊⊹ Sessão atualizada com sucesso! ₊⊹")
            time.sleep(1.5);
            questionary.print("Aguarde, redirecionando... ✮");
            return self.showSessionPage();