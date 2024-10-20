from movie import Movie
from pricing import REGULAR, NEW_RELEASE, CHILDREN
import logging
import datetime


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    REGULAR = REGULAR
    NEW_RELEASE = NEW_RELEASE
    CHILDRENS = CHILDREN

    def __init__(self, movie, price_code, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented
    
    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_price(self):
        """Calculates rental price based on it's price code."""
        return self.get_price_code().get_price(self.days_rented)

    def rental_points(self):
        return self.get_price_code().get_rental_points(self.days_rented)

    def price_code_for_movie(self, movie: Movie):
        year = datetime.date.today().year
        if movie.year == year:
            return NEW_RELEASE
        if any(g in ["Children", "Childrens"] for g in movie.genre):
            return CHILDREN
        return REGULAR
