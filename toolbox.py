import math

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line,Color

import fin

class ToolBox(BoxLayout):
	
	noofrooms =0

	list_of_rooms=[]
	statusvalue =0




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
	
		if noofrooms ==3:
			for x in xrange(statusvalue, nbyfn ):
				a = list_of_rooms[statusvalue]
				b = list_of_rooms[statusvalue +1]
				c = list_of_rooms[statusvalue +2]


			with ds.canvas:
				ds.canvas.clear()
				Color(1,0,0)
				Line(rectangle=a )
				Line(rectangle=b )
				Line(rectangle=c )

		elif noofrooms ==4:
			for x in xrange(statusvalue, nbyfn ):
				a = list_of_rooms[statusvalue]
				b = list_of_rooms[statusvalue +1]
				c = list_of_rooms[statusvalue +2]
				d = list_of_rooms[statusvalue +3]

			with ds.canvas:				
				ds.canvas.clear()
				Color(0,1,0)
				Line(rectangle=a )
				Line(rectangle=b )
				Line(rectangle=c )
				Line(rectangle=d )

		elif noofrooms ==5:
			for x in xrange(statusvalue, nbyfn ):
				a = list_of_rooms[statusvalue]
				b = list_of_rooms[statusvalue +1]
				c = list_of_rooms[statusvalue +2]
				d = list_of_rooms[statusvalue +3]
				e = list_of_rooms[statusvalue +4]

			with ds.canvas:
				ds.canvas.clear()
				Color(0,0,1)				
				Line(rectangle=a )
				Line(rectangle=b )
				Line(rectangle=c )
				Line(rectangle=d )
				Line(rectangle=e)
		elif noofrooms ==6:
			for x in xrange(statusvalue, nbyfn ):
				a = list_of_rooms[statusvalue]
				b = list_of_rooms[statusvalue +1]
				c = list_of_rooms[statusvalue +2]
				d = list_of_rooms[statusvalue +3]
				e = list_of_rooms[statusvalue +4]
				f = list_of_rooms[statusvalue +5]

			with ds.canvas:
				
				ds.canvas.clear()
				Color(1,0,1)
				Line(rectangle=a )
				Line(rectangle=b )
				Line(rectangle=c )
				Line(rectangle=d )
				Line(rectangle=e )
				Line(rectangle=f )

		elif noofrooms ==7:
			for x in xrange(statusvalue, nbyfn ):
				a = list_of_rooms[statusvalue]
				b = list_of_rooms[statusvalue +1]
				c = list_of_rooms[statusvalue +2]
				d = list_of_rooms[statusvalue +3]
				e = list_of_rooms[statusvalue +4]
				f = list_of_rooms[statusvalue +5]
				g = list_of_rooms[statusvalue +6]

			with ds.canvas:
				
				ds.canvas.clear()
				Color(0,1,1)
				Line(rectangle=a )
				Line(rectangle=b )
				Line(rectangle=c )
				Line(rectangle=d )
				Line(rectangle=e)
				Line(rectangle=f )
				Line(rectangle=g )
		#next value can be 1(next) or 2(prev) 	

		if next ==0:
			self.statusvalue = 0
		elif next == 1:
			# if statusvalue >= noofrooms:
			# 	self.statusvalue=0
			# else:
			self.statusvalue = statusvalue + noofrooms
		elif next == 2:
			# if statusvalue <= noofrooms:
			# 	self.statusvalue=0
			# else:
			self.statusvalue = statusvalue - noofrooms
		else:
			print "Status Value OutofBounds Error :)"

