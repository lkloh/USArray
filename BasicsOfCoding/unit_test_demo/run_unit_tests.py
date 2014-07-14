import unittest
from unit_tests.test_simple_calculator import calculatorModel, calculatorView

"""setup"""
calculator_model = unittest.TestLoader().loadTestsFromTestCase(calculatorModel)
calculator_view = unittest.TestLoader().loadTestsFromTestCase(calculatorView)


"""Run the models"""
unittest.TextTestRunner(verbosity=2).run(calculator_model)
unittest.TextTestRunner(verbosity=2).run(calculator_view)
