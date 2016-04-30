import math

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line,Color

import fin

class ToolBox(BoxLayout):
	
	noofrooms =0

	list_of_rooms=[]
	statusvalue =0
	list_of_plans =[]




	def calculate(self,rooms,next):	
		noofrooms = self.noofrooms = int(self.rooms.text)
		generatebutton = self.generatebutton
		
		self.list_of_rooms = fin.generateroom(noofrooms)
		
		self.draw(self.tool_box,next)

	def draw(self,tb,next):
		#nbyfn is the n * factorial of n
		noofrooms = self.noofrooms 
		nbyfn = noofrooms * math.factorial(noofrooms)
		print noofrooms," ",nbyfn ,"ddd" 
		statusvalue = self.statusvalue
		#reference the drawing space 
		ds = self.parent.drawing_space
		list_of_rooms = self.list_of_rooms
			
		print nbyfn 
		print "value of next: " ,next


		#this draws the plan taking exactly the number of rooms
		with ds.canvas:				
			ds.canvas.clear()
			Color(0,1,0)
			#for q in xrange(statusvalue, nbyfn ):
			for x in xrange(0,noofrooms ):
				print self.statusvalue + x
				Line(rectangle=list_of_rooms[self.statusvalue +x])
				print "coordinates used are : " ,x ," " ,list_of_rooms[self.statusvalue + x]

		#check the status value which points to the list of rooms array if it exeeds or is less update status value header
		if next ==0:
			self.statusvalue = statusvalue + noofrooms
		elif next == 1:
			if statusvalue > nbyfn:
				self.statusvalue=0
			else:
				self.statusvalue = statusvalue + noofrooms
		elif next == 2:
			if statusvalue < nbyfn:
				self.statusvalue=0
			else:
				self.statusvalue = statusvalue - noofrooms
		else:
			print "Status Value OutofBounds Error :)"

		
		#next value can be 1(next) or 2(prev) 	
		print "current statusvalue is " , statusvalue



# class room(Widget):
# 	