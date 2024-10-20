from movie import Movie
import csv


class MovieCatalog:
    def __init__(self):
        self.known_movies = []
        self.generator = self.movie_generator()

    def make_movie(self, movie: list[str, int]):
        columns = {'id': 0,
                   'title': 1,
                   'year': 2,
                   'genre': 3}
        return Movie(movie[columns['title']],
                     movie[columns['year']],
                     movie[columns['genre']].split('|'))

    def movie_generator(self):
        with open('movies.csv', 'r') as file:
            csv_file = csv.reader(file)
            for movie in csv_file:
                new_movie = self.make_movie(movie)
                self.known_movies += [new_movie]
                yield new_movie
            file.close()
            return None

    def get_movie(self, movie_name: str, movie_year: int = None):

        def is_the_movie(movie: Movie):
            if (movie.title == movie_name and
                    movie_year is None):
                return True
            if (movie.title == movie_name and
                    movie.year == movie_year):
                return True
            return False

        for movie in self.known_movies:
            if is_the_movie(movie):
                return movie
        for movie in self.generator:
            if is_the_movie(movie):
                return movie
        return None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MovieCatalog, cls).__new__(cls)
        return cls.instance
