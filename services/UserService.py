from database.database import connection,Database,Roles
class UserService:
    
    def registerUser(obj):
      obj['role'] = Roles.COMMON;
         
      print('USUÁRIO ', obj)
      Database.insert(connection.tb_user,obj);
      return Database.authenticateUser(connection.tb_user,obj);
    
    def authenticateUser(obj):
      return Database.authenticateUser(connection.tb_user,obj);
    
    def getUser(obj):
      return Database.get(connection.tb_user,obj);

    def deleteUser(obj,idUser):
      return Database.delete(connection.tb_user,idUser);
    
    def updateUser(obj,idUser):
          return Database.update(connection.tb_user,idUser,obj);
    
    def checkIfUserIsAdmin(obj):
      return Database.userIsAdmin(obj);