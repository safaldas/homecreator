import math

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line,Color

import fin

class ToolBox(BoxLayout):
	
	noofrooms =0

	list_of_rooms=[]
	statusvalue =0
	list_of_plans =[]
	# def __init__(self,**kwargs):
	# 	for y in xrange(0,400,10):
	# 		for x in xrange(0,600,10):
	# 			with self.drawing_space.canvas:
	# 				Color(0, 1, 0, .2)
	# 				Line(rectangle=[x,y,10,10])





	def calculate(self,rooms,next):	
		noofrooms = self.noofrooms = int(self.rooms.text)
		generatebutton = self.generatebutton
		self.statusvalue = 0
		print "new generate function called and statusvalue is ", self.statusvalue
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
			
		
		print "value of next: " ,next


		#this draws the plan taking exactly the number of rooms
		with ds.canvas:				
			ds.canvas.clear()
			Color(0,1,0)
			#for q in xrange(statusvalue, nbyfn ):
			for x in xrange(0,noofrooms ):
				print statusvalue + x
				Line(rectangle=list_of_rooms[statusvalue +x])
				print "coordinates used are : " ,x ," " ,list_of_rooms[statusvalue + x]

		#check the status value which points to the list of rooms array if it exeeds or is less update status value header
		if next ==0:
			self.statusvalue = statusvalue + noofrooms
			statusvalue += noofrooms
		elif next == 1:
			self.statusvalue = statusvalue + noofrooms
			statusvalue += noofrooms
			if self.statusvalue >= nbyfn:
				self.statusvalue=0
				statusvalue = 0
				print "going back"

		elif next == 2:
			
			if self.statusvalue <= 0:
				self.statusvalue=nbyfn
				statusvalue=nbyfn
				print "going to start value"
			self.statusvalue = statusvalue - noofrooms
			statusvalue -= noofrooms	
		else:
			print "next invalid:)"
		

		
		#next value can be 1(next) or 2(prev) 	
		print "current statusvalue is " , statusvalue
		print "current self.statusvalue is:" , self.statusvalue



