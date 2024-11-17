import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
       
    # Add your additional test cases here.
    def test_error_case(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), ValueError)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    
    def test_middle_age_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_elderly_age_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()