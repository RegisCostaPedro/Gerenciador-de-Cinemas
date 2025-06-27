from services.RoomService import RoomService;
from services.MovieService import MovieService;
from database.database import connection, Database;

class SessionService:

    def registerSession(obj):
       obj['id'] = Database.getNewID(connection.tb_session);
       return Database.insert(connection.tb_session, obj);
       
    def getSessions():
      sessionsList = Database.get(connection.tb_session);
      return sessionsList;

    def getDisponibleSessions():
      sessionsList = Database.get(connection.tb_session);

      disponibleSessionsList = [];

      for session in sessionsList:
        room = RoomService.getRoomById(session.get('room_id'));
        if (len(session.get('users')) < int(room.get('seatsQuantity'))):
          disponibleSessionsList.append(session);

      return disponibleSessionsList;

    def getSessionsJoin(sessionList):
      roomsList = RoomService.getRooms();
      moviesList = MovieService.getMovies();

      sessionsList = Database.get(connection.tb_session);
      response = [];

      for session in sessionsList:
        sessionObj = {};
        sessionObj['id'] = session.get('id');
        sessionObj['date'] = session.get('date');

        for room in roomsList:
          if (room.get('id') == session.get('room_id')):
            sessionObj['room'] = room.get('name');

        for movie in moviesList:
          if (movie.get('id') == session.get('movie_id')):
            sessionObj['movie'] = movie.get('name');

        response.append(sessionObj);
      
      return response;

    def getDisponibleSessionsJoin():
      roomsList = RoomService.getRooms();
      moviesList = MovieService.getMovies();

      sessionsList = SessionService.getDisponibleSessions();
      response = [];

      for session in sessionsList:
        sessionObj = {};
        sessionObj['id'] = session.get('id');
        sessionObj['date'] = session.get('date');
        sessionObj['users'] = session.get('users');

        for room in roomsList:
          if (room.get('id') == session.get('room_id')):
            sessionObj['room'] = room.get('name');

        for movie in moviesList:
          if (movie.get('id') == session.get('movie_id')):
            sessionObj['movie'] = movie.get('name');

        response.append(sessionObj);
      
      return response;

    def deleteSession(id):
        return Database.delete(connection.tb_session, id);

    def updateSession(id, obj):
        return Database.update(connection.tb_session, id, obj);

    def addUserInSession(sessionId, userId):
      session = Database.getById(connection.tb_session, sessionId);
      sessionUsers = session.get('users');
      sessionUsers.append(userId);

      session.update({ "users": sessionUsers });
      SessionService.updateSession(sessionId, session);
      print(connection.tb_session);

    def getUserSessions(userId):
      sessionsList = SessionService.getDisponibleSessionsJoin();
      userSessions = [session for session in sessionsList if userId in session.get('users')];
      return userSessions;
    

