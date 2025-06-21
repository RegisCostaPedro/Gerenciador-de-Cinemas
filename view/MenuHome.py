import questionary
from services.UserService import UserService;
from database.database import connection,Database

class Home:
    def showMenuHome(self):

        choice =  questionary.select(
           "O Que Você Deseja Acessar Hoje?",
           
            choices=[
                'Filmes em Cartaz',
                'Comprar Ingressos',
                'Minhas Sessões',
                'Sair'
            ],
            qmark="✮",
            
        ).ask();
       
        if choice == "Sair":
            question = questionary.select("Deseja Mesmo Sair?",choices=[
                "Sim","Não"
            ], qmark="✮").ask();
           