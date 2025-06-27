from enum import Enum;

class Roles(Enum):
    COMMON = 0; 
    ADMIN = 1;
    

class Database:
    def __init__(self, tb_user, tb_movie, tb_room, tb_session):
        self.tb_user = tb_user;
        self.tb_movie = tb_movie;
        self.tb_room = tb_room;
        self.tb_session = tb_session;

    @staticmethod
    def insert(table, obj):
        table.append(obj);
        return True;
   
    @staticmethod
    def get(table):
        result = []
        for register in table:
            result.append(register)
        return result    

    @staticmethod
    def getById(table):
        for register in table:
            if (register.get('id') == id):
                 return register;
        return False;

    @staticmethod
    def update(table, id, obj):
        for register in table:
            if (register.get('id') == id):
                 register.update(obj);
                 return  True;

    @staticmethod
    def delete(table, id):
        for register in table:
            if (register.get('id') == id):
                    table.remove(register);
                    return True
                   
        
    @staticmethod
    def getNewID(table):
        try:
            lastIndex = table[len(table) - 1];
            return table[len(table) - 1].get('id') + 1;
        except:
            return 1;

        
    @staticmethod
    def authenticateUser(tb_user, userObj):
        for user in tb_user:
            if (user.get('login') == userObj.get('login') and user.get('password') == userObj.get('password')):
                return user;
        return False;

    @staticmethod
    def userIsAdmin(userObj):
        if (userObj.get('role').value != 1): return False;
        return True;

# Iniciando banco de dados com as tabelas vazias
connection = Database([], [], [], []);

# Criando usuário Admin
Database.insert(connection.tb_user, {
    'id': 1,
    'login': 'admin',
    'password': 'admin',
    'role': Roles.ADMIN
});