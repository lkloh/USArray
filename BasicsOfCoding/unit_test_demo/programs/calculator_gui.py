import numpy 
import matplotlib 
matplotlib.use('tkagg')
import matplotlib.pyplot as py

class CalculatorGUI:

	def __init__(self):
		self.setup_gui()
		py.show()

	def setup_gui(self):
		fig = py.figure('Calculator')

		xx = 0.4
		yy = 0.1
		xm = 0.1
		diff = 0.15

		axs = {}
		axs['+'] = fig.add_axes([xm, diff*1, xx, yy])
		axs['-'] = fig.add_axes([xm, diff*2, xx, yy])




