from movie import Movie
import csv


class MovieCatalog:
    def get_movie(self, movie_name: str, movie_year: int = None):
        return_movie = None
        columns = {'id': 0,
                   'title': 1,
                   'year': 2,
                   'genre': 3}
        with open('movies.csv', 'r') as file:
            csv_file = csv.reader(file)
            for movie in csv_file:
                if '#' in movie[0] or not movie:
                    continue
                if (movie[columns['title']] == movie_name and
                        movie_year is None):
                    return_movie = movie
                    break
                if (movie[columns['title']] == movie_name and
                        movie[columns['year']] == movie_year):
                    return_movie = movie
                    break
            file.close()
        if return_movie:
            return_movie = Movie(return_movie[columns['title']],
                                 return_movie[columns['year']],
                                 return_movie[columns['genre']].split('|'))
        return return_movie

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MovieCatalog, cls).__new__(cls)
        return cls.instance
