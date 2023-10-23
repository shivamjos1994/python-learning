import unittest
from prime import is_prime

class Test(unittest.TestCase):
    def test_2(self):
        # checks that 2 is prime
        self.assertFalse(is_prime(2))

    def test_7(self):
        # checks that 2 is prime
        self.assertTrue(is_prime(7))

    def test_6(self):
        # checks that 6 is not prime
        self.assertFalse(is_prime(6))

    def test_11(self):
        # checks that 11 is prime
        self.assertTrue(is_prime(11))

    def test_20(self):
        # checks that 20 is not prime
        self.assertFalse(is_prime(20))

unittest.main()