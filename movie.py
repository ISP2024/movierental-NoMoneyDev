from dataclasses import dataclass


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

    def __str__(self):
        return f"{self.get_title} ({self.year})"
