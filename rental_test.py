import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, [])
        self.regular_movie = Movie("Air", 2020, [])
        self.childrens_movie = Movie("Frozen", 2020, ['Childrens'])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2020, [])
        self.assertEqual("Air", m.get_title())

    # @unittest.skip("add this test when you refactor rental price")
    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_price(), 6.5)
        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)
        # self.fail("TODO add more tests for other movie categories")

    # @unittest.skip("add this test of rental points when you add it to Rental")
    def test_rental_points(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.rental_points(), 5)
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.rental_points(), 1)
        # self.fail("add this test of frequent renter points")
