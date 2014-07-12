import matplotlib 
matplotlib.use('tkagg')
from programs.simple_calculator import add, subtract, times, divide 
from programs.calculator_gui import CalculatorGUI

def main():
	CalculatorGUI()

if __name__ == "__main__":
	main()
