import unittest
from test_f import my_plus
class TestPlus(unittest.TestCase):
    def test_1(self):
        self.assertEqual(my_plus(1,2),3) 
    def test_2(self):
        self.assertEqual(my_plus(1,-2),1)  # failed
    def setUp(self):
        self.testplus = my_plus(4,5)
    def test_3(self):
        self.assertEqual(self.testplus,9) 