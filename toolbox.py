#v4 using the widget to create rooms
import math

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line,Color,Rectangle
from kivy.uix.widget import Widget
from kivy.graphics.context_instructions import PushMatrix,PopMatrix



class ToolBox(BoxLayout):
	
	def set_area(self):
		budget = self.budget
		area = self.area
		if int(budget.text) == 10:
			area.values =['600','650','700']
			area.text = '600'
			print 'area updated to ',area.text
		if int(budget.text) == 15:
			area.values =['750','800','850']
			area.text = '750'
			print 'area updated to ',area.text

		area.disabled = False


	def calculate(self):
		ds = self.parent.drawing_space

		bedroom1 = Widget(size = (100,100))
		with bedroom1.canvas:
			Rectangle(source="images/bedroom10x10.png", pos=bedroom1.pos,size=bedroom1.size)
			ds.add_widget(bedroom1)
		bedroom2 = Widget(size = (140,120))
		with bedroom2.canvas:
			Rectangle(source="images/bedroom14x12.png", pos=(100,0),size=bedroom2.size)
			ds.add_widget(bedroom2)