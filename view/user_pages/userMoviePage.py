import questionary
from services.MovieService import MovieService;
from helpers import clearScream

class UserMoviePage:
    def showMoviePage(self):
       
        clearScream.Helpers.clearScreen()
        questionary.print("⋆⭒˚｡⋆ Filmes em Cartaz ⋆⭒˚｡⋆\n\n")

        movieList = MovieService.getMovies();

        if movieList:
            for movies in movieList:
                print(f"Filme: {movies.get('name')}")
                print(f"Ano de Lançamento: {movies.get('releaseYear')}")
                print(f"Duração: {movies.get('duration')}")
                print(f"Categoria: {movies.get('category')}")
                print()
        else:
            print("Nenhum filme em cartaz...");

        print(".............................................................");
        questionary.confirm(message="←- Voltar",instruction=" (⏎)").ask()

        from view.menu.MenuHome import Home;
        home = Home();
        return home.showMenuHome();