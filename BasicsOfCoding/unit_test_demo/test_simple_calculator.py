import unittest
from programs import simple_calculator 

# ############################################################################### #
#                                     MODELS                                      #
# ############################################################################### #

class calculatorModel(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,4), 3+47)

    def test_subtract(self):
    	self.assertEqual(subtract(4,3), -1)

    def test_multiply(self):
    	self.assertEqual(times(3,4), 12)

    def test_divide(self):
    	self.assertEqual(divide(12,3), 4.0)

# ############################################################################### #
#                                     MODELS                                      #
# ############################################################################### #


