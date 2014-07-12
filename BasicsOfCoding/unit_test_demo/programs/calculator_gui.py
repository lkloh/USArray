import numpy 
import matplotlib 
matplotlib.use('tkagg')
import matplotlib.pyplot as py
from matplotlib.widgets import Button, RadioButtons 
from programs.simple_calculator import add, subtract, times, divide 

class CalculatorGUI:

	def __init__(self):
		self.setup_gui()
		self.connect_buttons()
		py.show()

	def save_action(self, event):
		print event

	def connect_buttons(self):
		"""add button"""
		self.bn_firstnum = RadioButtons(self.axs['firstnums'], (1,2,3,4,5), active=1)
		self.bn_secondnum = RadioButtons(self.axs['secondnums'], (1,2,3,4,5), active=1)
		self.bn_add = Button(self.axs['add'], '+')
		self.bn_subtract = Button(self.axs['subtract'], '-')
		self.bn_times = Button(self.axs['times'], 'x')
		self.bn_divide = Button(self.axs['divide'], '/')

		"""connecting"""
		self.cid_add = self.bn_add.on_clicked(self.save_action)
		self.cid_subtract = self.bn_subtract.on_clicked(self.save_action)
		self.cid_times = self.bn_times.on_clicked(self.save_action)
		self.cid_divide = self.bn_divide.on_clicked(self.save_action)

	def setup_gui(self):
		fig = py.figure('Calculator')

		xx = 0.1
		yy = 0.1
		xm = 0.1
		diff = 0.15

		axs = {}
		axs['firstnums'] = fig.add_axes([1*xm, diff*2, xx, yy])
		axs['secondnums'] = fig.add_axes([3*xm, diff*2, xx, yy])
		axs['add'] = fig.add_axes([2*xm, diff*1, xx, yy])
		axs['subtract'] = fig.add_axes([2*xm, diff*2, xx, yy])
		axs['times'] = fig.add_axes([2*xm, diff*3, xx, yy])
		axs['divide'] = fig.add_axes([2*xm, diff*4, xx, yy])

		self.axs = axs
		self.fig = fig 





