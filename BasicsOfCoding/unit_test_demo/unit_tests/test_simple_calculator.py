import unittest
import matplotlib
import matplotlib.pyplot as py
from programs.simple_calculator import add, subtract, times, divide 
from programs.calculator_gui import CalculatorGUI

# ############################################################################### #
#                                     MODELS                                      #
# ############################################################################### #

class calculatorModel(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,4), 3+4)

    def test_subtract(self):
    	self.assertEqual(subtract(4,3), 1)

    def test_multiply(self):
    	self.assertEqual(times(3,4), 12)

    def test_divide(self):
    	self.assertEqual(divide(12,3), 4.0)

# ############################################################################### #
#                                     MODELS                                      #
# ############################################################################### #


class calculatorView(unittest.TestCase):    
    
    def test_three_times_four(self):
        gui = CalculatorGUI()

        # click first number
        gui.get_first_num(3)

        # click the sort button
        event_operation = matplotlib.backend_bases.MouseEvent('button_press_event', gui.fig.canvas, 203, 236)
        gui.save_action(event_operation)

        # click second number
        gui.get_second_num(4)

        # click = sign
        event_compute = matplotlib.backend_bases.MouseEvent('button_press_event', gui.fig.canvas, 443, 164)
        gui.compute(event_compute)

        # check get expected result 
        print gui.bn_ans.label.get_text()
        self.assertEqual(gui.bn_ans.label.get_text(), '12')







