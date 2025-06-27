from typing import Any;

import questionary;
import questionary.question;
import time;
from services.RoomService import RoomService;
from database.database import connection, Database;
from helpers import clearScream;
     
class RoomPage:

    def showRoomPage(self):
        clearScream.Helpers.clearScreen();
        questionary.print(f" ˗ˏˋ Salas ⊹ ─                                ", style="blink fg:#fff bg:black bold")

        choices = [ 'Adicionar Sala', 'Listar Salas', 'Atualizar Sala', 'Remover Sala', 'Voltar' ];
        roomChoice = questionary.select(" ", choices=choices, qmark="✮").ask();

        match roomChoice:
            case "Adicionar Sala":
                return self.showRegisterRoomPage()
            case "Listar Salas":
                return self.showListRoomsPage()
            case 'Atualizar Sala':
                return self.showUpdateRoomPage()
            case 'Remover Sala':
                return self.showRemoveRoomPage()
            case 'Voltar':
                from view.menu.MenuHome import Home;
                home = Home();
                home.showMenuHomeAdmin();
                
    def showListRoomsPage(self):
        clearScream.Helpers.clearScreen(); 
        questionary.print("⋆⭒˚｡⋆ Salas ⋆⭒˚｡⋆\n\n");

        roomList = RoomService.getRooms();

        if roomList:
           for room in roomList:
            print(f"Id: {room.get('id')}");
            print(f"Nome: {room.get('name')}");
            print(f"Quantidade de Lugares: {room.get('seatsQuantity')}");
            print();
        else:
            print("Nenhuma sala registrada...");

        print(".............................................................")

        questionary.confirm(message="←- Voltar", instruction=" (⏎)").ask();
        return self.showRoomPage();
    
        
    def showRegisterRoomPage(self):
        clearScream.Helpers.clearScreen();
        questionary.print("Digite as Informações da Sala");

        roomObj = questionary.form(
            name = questionary.text("Nome: "),
            seatsQuantity = questionary.text("Quantidade de lugares: "),
        ).ask();

        RoomService.registerRoom(roomObj);

        questionary.print("✮ Sala salva com sucesso! ✮");
        questionary.print("Aguarde, redirecionando... ✮");
        time.sleep(1.5);
        self.showRoomPage();

    def showRemoveRoomPage(self):
        clearScream.Helpers.clearScreen();

        questionary.print("⋆⭒˚｡⋆ Salas ⋆⭒˚｡⋆\n\n");
        print();
        questionary.print("Selecione uma sala para excluir");
        print();
       
        roomList = RoomService.getRooms();

        if not roomList:
             questionary.print("Nenhuma sala registrada...");
             print();
             questionary.confirm(message="←- Voltar", instruction=" (⏎)").ask();
             return self.showRoomPage();
         
        choices = [f"{room.get('id')} - {room.get('name')}" for room in roomList];
        choices.append("←- Voltar");

        roomSelected= questionary.select(message="", choices=choices).ask();

        if roomSelected == "←- Voltar":
             return self.showRoomPage();
       
        print(".............................................................")
        
        idToDelete= roomSelected.split(' - ')[0];

        roomDeleted = RoomService.deleteRoom(int(idToDelete));
        
        if roomDeleted:
            questionary.print(" ✖ Sala removida!");
            time.sleep(1.5);
            questionary.print("Aguarde, redirecionando... ✮");
            return self.showRoomPage();
        
    def showUpdateRoomPage(self):
        clearScream.Helpers.clearScreen();
        questionary.print("⋆⭒˚｡⋆ Sals ⋆⭒˚｡⋆\n\n");
        questionary.print("Selecione uma sala para editar");
       
        roomList = RoomService.getRooms();

        if not roomList:
             questionary.print("Nenhuma sala registrada...");
             print();
             questionary.confirm(message="←- Voltar",instruction=" (⏎)").ask();
             return self.showRoomPage();
         
        for room in roomList:
            print(f"Id: {room.get('id')}");
            print(f"Nome: {room.get('name')}");
            print(f"Quantidade de Lugares: {room.get('seatsQuantity')}");
            print();

        choices = [f"{room.get('id')} - {room.get('name')}" for room in roomList];
        choices.append("←- Voltar");

        roomSelected= questionary.select(message="", choices=choices).ask();

        if roomSelected == "←- Voltar":
             return self.showRoomPage();
       
        print();
        print("⋆.˚ ──────────────────────── Atualize as Informações da Sala ─────────────────────── ⋆.˚\n")
        
        newRoomObj = questionary.form(
            name = questionary.text("Nome: "),
            seatsQuantity = questionary.text("Quantidade de lugares: "),
        ).ask();

        idToUpdate= roomSelected.split(' - ')[0];
        roomUpdated = RoomService.updateRoom(int(idToUpdate), newRoomObj);
        
        if roomUpdated:
            questionary.print(" ₊⊹ Sala atualizada com sucesso! ₊⊹")
            time.sleep(1.5);
            questionary.print("Aguarde, redirecionando... ✮");
            return self.showRoomPage();