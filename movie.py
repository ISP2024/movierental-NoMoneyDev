from dataclasses import dataclass
from pricing import REGULAR, NEW_RELEASE, CHILDREN
import datetime


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    # Initialize a new movie.
    title: str
    year: int
    genre: list[str]

    def get_title(self):
        return self.title

    def is_genre(self, check_genre):
        return check_genre.lower() in [g.lower() for g in self.genre]

    def price_code_for_movie(self):
        year = datetime.date.today().year
        if self.year == year:
            return NEW_RELEASE
        if any(g in ["Children", "Childrens"] for g in self.genre):
            return CHILDREN
        return REGULAR

    def __str__(self):
        return f"{self.get_title} ({self.year})"
