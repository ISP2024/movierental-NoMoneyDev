import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two")
        self.regular_movie = Movie("Air")
        self.childrens_movie = Movie("Frozen")

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air")
        self.assertEqual("Air", m.get_title())

    # @unittest.skip("add this test when you refactor rental price")
    def test_rental_price(self):
        rental = Rental(self.new_movie, Rental.NEW_RELEASE, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, Rental.NEW_RELEASE, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.regular_movie, Rental.REGULAR, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, Rental.REGULAR, 5)
        self.assertEqual(rental.get_price(), 6.5)
        rental = Rental(self.childrens_movie, Rental.CHILDRENS, 1)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, Rental.CHILDRENS, 5)
        self.assertEqual(rental.get_price(), 4.5)
        # self.fail("TODO add more tests for other movie categories")

    # @unittest.skip("add this test of rental points when you add it to Rental")
    def test_rental_points(self):
        rental = Rental(self.new_movie, Rental.NEW_RELEASE, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.new_movie, Rental.NEW_RELEASE, 5)
        self.assertEqual(rental.rental_points(), 5)
        rental = Rental(self.regular_movie, Rental.REGULAR, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.regular_movie, Rental.REGULAR, 5)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.childrens_movie, Rental.CHILDRENS, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.childrens_movie, Rental.CHILDRENS, 5)
        self.assertEqual(rental.rental_points(), 1)
        # self.fail("add this test of frequent renter points")

