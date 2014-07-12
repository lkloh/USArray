import unittest
from test_simple_calculator import calculatorModel


# ############################################################################### #
#                                     MODELS                                      #
# ############################################################################### #

"""Set the models"""
calculator_model = unittest.TestLoader().loadTestsFromTestCase(calculatorModel)

# ------------------------------------------------------------------------------- #

"""Run the models"""
unittest.TextTestRunner(verbosity=2).run(calculator_model)
