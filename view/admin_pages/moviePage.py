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
                'Atualizar Filme',
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
            case 'Atualizar Filme':
                return self.showUpdateMoviePage()
            case 'Remover Filme':
                return self.showRemoveMoviePage()
            case 'Voltar':
                from view.menu.MenuHome import Home
                home = Home()
                home.showMenuHomeAdmin();
                
    def showListMoviesPage(self):
        clearScream.Helpers.clearScreen()
        questionary.print("⋆⭒˚｡⋆ Filmes em Cartaz ⋆⭒˚｡⋆\n\n")

        movieList = MovieService.getMovies();

        if movieList:
            for movies in movieList:
                print(f"Id: {movies.get('id')}")
                print(f"Filme: {movies.get('name')}")
                print(f"Ano de Lançamento: {movies.get('releaseYear')}")
                print(f"Duração: {movies.get('duration')}")
                print(f"Categoria: {movies.get('category')}")
                print()
            else:
                print("Nenhum filme registrado...");

        print(".............................................................");
        
        questionary.confirm(message="←- Voltar",instruction=" (⏎)").ask()
        return self.showMoviePage()
    
        
    def showRegisterMoviePage(self):
        clearScream.Helpers.clearScreen()
        questionary.print("Digite as Informações do Filme")
        movieData = questionary.form(
            name=questionary.text("Nome: "),
            duration=questionary.text("Duração: "),
            category=questionary.text("Categoria: "),
            releaseYear=questionary.text("Ano de Lançamento: "),
        ).ask()
        movieSaved = MovieService.registerMovie(movieData)
        if movieSaved:
            questionary.print("✮ Filme salvo com sucesso! ✮")
            questionary.print("Aguarde, redirecionando... ✮");
            time.sleep(1.5)
            return self.showMoviePage()

    def showRemoveMoviePage(self):
        clearScream.Helpers.clearScreen()
        questionary.print("⋆⭒˚｡⋆ Filmes em Cartaz ⋆⭒˚｡⋆\n\n")
        questionary.print("Selecione um filme para excluir do catálogo")
       
        movieList = MovieService.getMovies();
        if not movieList:
             questionary.print("Nenhum filme disponível no catálogo.")
             questionary.confirm(message="←- Voltar",instruction=" (⏎)").ask()
             return self.showMoviePage()
         
        choices = [f"{movie.get('id')} - {movie.get('name')}" for movie in movieList]
        movieSelected= questionary.select(message="",choices=choices).ask()
       
        print(".............................................................")
        idToBeDeleted= movieSelected.split(' - ')[0]
        movieDeleted =MovieService.deleteMovie(int(idToBeDeleted));
        
        if movieDeleted:
            questionary.print(" ✖ Filme removido do catálogo!")
            time.sleep(1.5)
            return self.showMoviePage()
        
    def showUpdateMoviePage(self):
        clearScream.Helpers.clearScreen()
        questionary.print("⋆⭒˚｡⋆ Filmes em Cartaz ⋆⭒˚｡⋆\n\n")
        questionary.print("Selecione um filme no catálogo para editá-lo")
       
        movieList = MovieService.getMovies();
        if not movieList:
             questionary.print("Nenhum filme disponível no catálogo.")
             questionary.confirm(message="←- Voltar",instruction=" (⏎)").ask()
             return self.showMoviePage()
         
        for movies in movieList:
            print(f"Id: {movies.get('id')}")
            print(f"Filme: {movies.get('name')}")
            print(f"Ano de Lançamento: {movies.get('releaseYear')}")
            print(f"Duração: {movies.get('duration')}")
            print(f"Categoria: {movies.get('category')}")
            print();
        choices = [f"{movie.get('id')} - {movie.get('name')}" for movie in movieList]
        movieSelected= questionary.select(message="",choices=choices).ask()
       
        print("\n")
        print("⋆.˚ ──────────────────────── Atualize as Informações do Filme ─────────────────────── ⋆.˚\n")
        
        movieData = questionary.form(
                    name=questionary.text("Nome: "),
                    duration=questionary.text("Duração: "),
                    category=questionary.text("Categoria: "),
                    releaseYear=questionary.text("Ano de Lançamento: "),
                ).ask()
        idToBeUpdated= movieSelected.split(' - ')[0]
        movieUpdate =MovieService.updateMovie(int(idToBeUpdated),movieData);
        
        if movieUpdate:
            questionary.print(" ₊⊹ Filme atualizado com sucesso! ₊⊹")
            time.sleep(1.5)
            return self.showMoviePage()