import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", 2024, [])
        self.regular_movie = Movie("CitizenFour", 2020, [])
        self.childrens_movie = Movie("Frozen", 2020, ['Childrens'])

    @unittest.skip("No convenient way to test")
    def test_billing():
        # no convenient way to test billing since its buried in the statement() method.
        pass

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_total_charge(self):
        self.c.add_rental(Rental(self.new_movie, 4))
        self.c.add_rental(Rental(self.regular_movie, 4))
        self.c.add_rental(Rental(self.childrens_movie, 4))
        total_charge = self.c.total_amount()
        self.assertEqual(total_charge, 20)

    def test_total_rental_points(self):
        self.c.add_rental(Rental(self.new_movie, 4))
        self.c.add_rental(Rental(self.regular_movie, 4))
        self.c.add_rental(Rental(self.childrens_movie, 4))
        rental_points = self.c.get_rental_point()
        self.assertEqual(rental_points, 6)
