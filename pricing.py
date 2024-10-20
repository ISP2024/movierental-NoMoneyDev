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