# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from rental import Rental
from customer import Customer
from movie_catalog import MovieCatalog


def make_movies(catalog):
    """Some sample movies."""
    movies = [
        catalog.get_movie("Air"),
        catalog.get_movie("Oppenheimer"),
        catalog.get_movie("Frozen"),
        catalog.get_movie("Bitconned"),
        catalog.get_movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    catalog = MovieCatalog()
    days = 1
    for movie in make_movies(catalog):
        if movie:
            customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
