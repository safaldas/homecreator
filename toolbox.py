#v4 using the widget to create rooms
import math

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line,Color,Rectangle
from kivy.uix.widget import Widget
from kivy.graphics.context_instructions import PushMatrix,PopMatrix

import rooms 

class ToolBox(BoxLayout):
	
	def set_area(self):
		budget = self.budget
		area = self.area
		if int(budget.text) == 10:
			area.values =['600','650','700']
			area.text = '600'
			print 'area updated to ',area.text
		elif int(budget.text) == 15:
			area.values =['750','800','850']
			area.text = '750'
			print 'area updated to ',area.text
		elif int(budget.text) == 20:
			area.values =['900','950','1000']
			area.text = '900'
			print 'area updated to ',area.text
		elif int(budget.text) == 30:
			area.values =['1100','1200','1300']
			area.text = '1100'
			print 'area updated to ',area.text
		else:
			print "budget not defined cant update area"
		print area.text
		area.disabled = False


	def calculate(self):
		ds = self.parent.drawing_space

		room1 = rooms.bedroom()
		room1.draw(1)
		ds.add_widget(room1)
		