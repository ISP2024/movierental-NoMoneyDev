from abc import ABC, abstractmethod


class PriceStrategy(ABC):

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass

    @classmethod
    def __new__(cls, *args):
        try:
            return cls._instance
        except AttributeError:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
            return cls._instance


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return days

    def get_price(self, days):
        return 3 * days


class RegularPrice(PriceStrategy):
    """Pricing rules for Relugar movies."""

    def get_rental_points(self, days: int) -> int:
        return 1

    def get_price(self, days: int) -> float:
        price = 2
        add_per_day = 1.5
        for_days = 2
        if days-for_days <= 0:
            return price
        return price + (days-for_days)*add_per_day


class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children movies."""

    def get_rental_points(self, days: int) -> int:
        return 1

    def get_price(self, days: int) -> float:
        price = 1.5
        for_days = 3
        add_per_day = 1.5
        if days <= for_days:
            return price
        return price + (days-for_days)*add_per_day


NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    REGULAR = REGULAR
    NEW_RELEASE = NEW_RELEASE
    CHILDRENS = CHILDREN

    def __init__(self, title, price_code):
        # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_rental_points(self, days: int):
        return self.get_price_code().get_rental_points(days)

    def get_price(self, days: int):
        return self.get_price_code().get_price(days)

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
