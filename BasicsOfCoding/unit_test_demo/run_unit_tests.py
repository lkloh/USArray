import unittest
from unit_tests.test_simple_calculator import calculatorModel


"""setup"""
calculator_model = unittest.TestLoader().loadTestsFromTestCase(calculatorModel)



"""Run the models"""
unittest.TextTestRunner(verbosity=2).run(calculator_model)
