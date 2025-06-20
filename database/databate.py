from enum import Enum;


class Roles(Enum):
    COMMON = 1; 
    ADMIN = 1;
    

class Database:
    def __init__(self, tb_user,tb_movie,tb_catalog,tb_room,tb_session):
        self.tb_user = tb_user;
        self.tb_movie = tb_movie;
        self.tb_catalog = tb_catalog;
        self.tb_room = tb_room;
        self.tb_session = tb_session;

    def insert(self,table,obj):
        table.append(obj);
   
    def get(self,table):
        for register in table:
            for key,value in register.items():
                print(f"{key}: {value}");
            
        print();
        
connection = Database([
    {
        "login": "admin",
        "password": "admin",
        "role": Roles.ADMIN.name 
    }
    ],[],[],[],[]);

   