import unittest
from unit_test_demo.programs.simple_calculator import add 


# ############################################################################### #
#                                     MODELS                                      #
# ############################################################################### #

class calculatorModel(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,4), 3+4)

    def test_subtract(self):
    	self.assertEqual(add(4,3), 4-3)

    def test_multiply(self):
    	self.assertEqual(multiply(3,4), 3*4)

    def test_divide(self):
    	self.assertEqual(divide(12,3), 12/float(3))

# ############################################################################### #
#                                     MODELS                                      #
# ############################################################################### #


