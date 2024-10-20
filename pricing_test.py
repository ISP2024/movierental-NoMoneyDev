import unittest
from movie import Movie
from rental import REGULAR, NEW_RELEASE, CHILDREN


class PricingCodeTest(unittest.TestCase):
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, [])
        self.regular_movie = Movie("Air", 2020, [])
        self.childrens_movie = Movie("Frozen", 2020, ['Childrens'])

    def test_get_pricing_code(self):
        self.assertEqual(NEW_RELEASE, self.new_movie.price_code_for_movie())
        self.assertEqual(REGULAR, self.regular_movie.price_code_for_movie())
        self.assertEqual(CHILDREN, self.childrens_movie.price_code_for_movie())
