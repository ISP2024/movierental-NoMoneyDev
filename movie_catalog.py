from movie import Movie
import csv
import logging


logger = logging.getLogger()
logFormatter = logging.Formatter(
    fmt='Line %(lineno)d: Unrecognized format "%(message)s"')
filehandler = logging.FileHandler('movie_log.log', 'w')
filehandler.setFormatter(logFormatter)
logger.addHandler(filehandler)


class MovieCatalog:
    columns = {'id': 0,
               'title': 1,
               'year': 2,
               'genre': 3}
    
    def __init__(self):
        self.known_movies = []
        self.generator = self.movie_generator()

    def make_movie(self, movie: list[str, int]):
        columns = MovieCatalog.columns
        return Movie(movie[columns['title']],
                     movie[columns['year']],
                     movie[columns['genre']].split('|'))

    def valid_line(self, movie: list[str, int]):
        columns = MovieCatalog.columns
        if '#' in movie[0]:  # Comment line
            return False
        if not movie[columns['year']].isnumeric():
            logger.error(', '.join(movie))
            return False
        if len(movie) != 4:
            logger.error(', '.join(movie))
            return False
        return True

    def movie_generator(self):
        with open('movies.csv', 'r') as file:
            csv_file = csv.reader(file)
            for movie in csv_file:
                if not self.valid_line(movie):
                    continue
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
