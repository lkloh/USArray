import numpy 
import matplotlib 
matplotlib.use('tkagg')
import matplotlib.pyplot as py
from matplotlib.widgets import Button
from programs.simple_calculator import add, subtract, times, divide 

class CalculatorGUI:

	def __init__(self):
		self.setup_gui()
		self.connect_buttons()
		py.show()



	def connect_buttons(self):
		self.bn_add = Button(self.axs['add'], '+')
		self.bn_subtract = Button(self.axs['subtract'], '-')
		self.bn_times = Button(self.axs['times'], 'x')
		self.bn_divide = Button(self.axs['divide'], '/')

		self.cid_add = self.bn_add.on_clicked(add(3,4))

	def setup_gui(self):
		fig = py.figure('Calculator')

		xx = 0.1
		yy = 0.1
		xm = 0.1
		diff = 0.15

		axs = {}
		axs['add'] = fig.add_axes([xm, diff*1, xx, yy])
		axs['subtract'] = fig.add_axes([xm, diff*2, xx, yy])
		axs['times'] = fig.add_axes([xm, diff*3, xx, yy])
		axs['divide'] = fig.add_axes([xm, diff*4, xx, yy])

		self.axs = axs
		self.fig = fig 





