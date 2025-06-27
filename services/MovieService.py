from database.database import connection, Database, Roles

class MovieService:

    def registerMovie(obj):
       obj['id'] = Database.getNewID(connection.tb_movie);
       return Database.insert(connection.tb_movie, obj);
       
    def getMovies():
      movieList = Database.get(connection.tb_movie)
      if movieList and len(movieList) > 0:
        return movieList
      else:
        return []

    def deleteMovie(idMovie):
        return Database.delete(connection.tb_movie, idMovie);
    def updateMovie(idMovie,obj):
        return Database.update(connection.tb_movie, idMovie,obj);

