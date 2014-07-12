import numpy 
import matplotlib 
matplotlib.use('tkagg')
import matplotlib.pyplot as py
from matplotlib.widgets import Button, RadioButtons 
from programs.simple_calculator import add, subtract, times, divide 

class CalculatorGUI:

	def __init__(self):
		self.set_defaults()
		self.setup_gui()
		self.connect_buttons()
		py.show()

	def set_defaults(self):
		self.firstnum = ''
		self.secondnum = ''
		self.operation = ''

	def save_action(self, event):
		if event.inaxes==self.axs['add']:
			operation = 'add'
		elif event.inaxes==self.axs['subtract']:
			operation == 'subtract'
		elif event.inaxes==self.axs['times']:
			operation = 'times'
		elif event.inaxes==self.axs['divide']:
			operation = 'divide'
		self.operation = operation

	def get_first_num(self, event):
		self.firstnum = event
		self.bn_firstnum.disconnect(self.cid_firstnum)

	def get_second_num(self, event):
		self.secondnum = event

	def disconnect_all(self, event):
		self.bn_secondnum.disconnect(self.cid_secondnum)
		self.bn_firstnum.disconnect(self.cid_firstnum)

	def compute(self, event):
		if self.operation != '' and self.firstnum != '' and self.secondnum != '':
			if self.operation == 'add':
				answer = add(int(self.firstnum), int(self.secondnum))
			elif self.operation == 'subtract':
				answer = subtract(int(self.firstnum), int(self.secondnum))
			elif self.operation == 'times':
				answer = times(int(self.firstnum), int(self.secondnum))
			elif self.operation == 'divide':
				answer = divide(int(self.firstnum), int(self.secondnum))
			self.bn_ans.label.set_text(answer)

	def connect_buttons(self):
		"""add button"""
		self.bn_firstnum = RadioButtons(self.axs['firstnums'], (1,2,3,4,5), active=0)
		self.bn_secondnum = RadioButtons(self.axs['secondnums'], (1,2,3,4,5), active=0)
		self.bn_add = Button(self.axs['add'], '+')
		self.bn_subtract = Button(self.axs['subtract'], '-')
		self.bn_times = Button(self.axs['times'], 'x')
		self.bn_divide = Button(self.axs['divide'], '/')
		self.bn_equal = Button(self.axs['equal'],'=')
		self.bn_ans = Button(self.axs['ans'],'ANS')

		"""connecting"""
		self.cid_add = self.bn_add.on_clicked(self.save_action)
		self.cid_subtract = self.bn_subtract.on_clicked(self.save_action)
		self.cid_times = self.bn_times.on_clicked(self.save_action)
		self.cid_divide = self.bn_divide.on_clicked(self.save_action)
		self.cid_firstnum = self.bn_firstnum.on_clicked(self.get_first_num)
		self.cid_secondnum = self.bn_secondnum.on_clicked(self.get_second_num)
		self.cid_equal = self.bn_equal.on_clicked(self.compute)

	def setup_gui(self):
		fig = py.figure('Calculator')

		xx = 0.1
		yy = 0.1
		xm = 0.09
		diff = 0.15

		axs = {}
		axs['firstnums'] = fig.add_axes([1*xm, diff*2, xx, 2*yy])
		axs['add'] = fig.add_axes([3*xm, diff*1, xx, yy])
		axs['subtract'] = fig.add_axes([3*xm, diff*2, xx, yy])
		axs['times'] = fig.add_axes([3*xm, diff*3, xx, yy])
		axs['divide'] = fig.add_axes([3*xm, diff*4, xx, yy])
		axs['secondnums'] = fig.add_axes([5*xm, diff*2, xx, 2*yy])
		axs['equal'] = fig.add_axes([7*xm, diff*2, xx, yy])
		axs['ans'] = fig.add_axes([9*xm, diff*2, xx, yy])

		self.axs = axs
		self.fig = fig 





