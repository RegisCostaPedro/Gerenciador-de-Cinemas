from database.database import connection, Database, Roles

class RoomService:

    def registerRoom(obj):
       obj['id'] = Database.getNewID(connection.tb_room);
       return Database.insert(connection.tb_room, obj);
       
    def getRooms():
      roomList = Database.get(connection.tb_room);
      return roomList;

    def deleteRoom(id):
        return Database.delete(connection.tb_room, id);

    def updateRoom(id, obj):
        return Database.update(connection.tb_room, id, obj);

