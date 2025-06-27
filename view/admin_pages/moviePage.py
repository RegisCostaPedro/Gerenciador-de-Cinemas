from typing import Any

import questionary
import questionary.question
from services.MovieService import MovieService;
from database.database import connection, Database
import time
from helpers import clearScream

     

class MoviePage:
    def showMoviePage(self):
       
        clearScream.Helpers.clearScreen()
        questionary.print(f" ˗ˏˋ Filmes ⊹ ─                                ", style="blink fg:#fff bg:black bold")
      
        movieChoice = questionary.select(
            " ",
            choices=[
                'Adicionar Filme',
                'Listar Filmes',
                'Remover Filme',
                'Voltar'
            ],
            qmark="✮",
        ).ask()

        match movieChoice:
            case "Adicionar Filme":
                return self.showRegisterMoviePage()
            case "Listar Filmes":
                return self.showListMoviesPage()
            case 'Remover Filme':
                return self.showRemoveMoviePage()
            case 'Voltar':
                from view.menu.MenuHome import Home
                home = Home()
                home.showMenuHomeAdmin();
                
    def showListMoviesPage(self):
        clearScream.Helpers.clearScreen()
        questionary.print("⋆⭒˚｡⋆ Filmes em Cartaz ⋆⭒˚｡⋆\n\n")
        print(".............................................................")
        MovieService.getMovies();
        print(".............................................................")
        questionary.confirm(message="←- Voltar",instruction=" (⏎)").ask()
        return self.showMoviePage()
      
        
    def showRegisterMoviePage(self):
        clearScream.Helpers.clearScreen()
        questionary.print("Digite as Informações do Filme")
        movieData = questionary.form(
            nome=questionary.text("Nome: "),
            duracao=questionary.text("Duração: "),
            categoria=questionary.text("Categoria: "),
            ano=questionary.text("Ano de Lançamento: "),
        ).ask()
        movieSaved = MovieService.registerMovie(movieData)
        if movieSaved:
            questionary.print("Filme salvo com sucesso! ✮")
            time.sleep(2)
            return self.showMoviePage()

    def showRemoveMoviePage(self):
        clearScream.Helpers.clearScreen()
        questionary.print("⋆⭒˚｡⋆ Filmes em Cartaz ⋆⭒˚｡⋆\n\n")
        questionary.print("Selecione um filme para excluir do catálogo")
        print(".............................................................")
        
      
        
        print(".............................................................")
        