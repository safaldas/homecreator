from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line,Color

class GeneralArea(RelativeLayout):
	# def __init__(self,**kwargs):
	# 	super(GeneralArea,self).__init__ ( **kwargs)
		
	# 	for y in xrange(0,400,10):
	# 		for x in xrange(0,600):
	# 			with self.drawing_space.canvas:
	# 				Line(rectangle=[x,y,10,10])
			
	def load_next(self):			
		tool_box= self.tool_box
		next = self.next
		for y in xrange(0,400,10):
			for x in xrange(0,600,10):
				with self.drawing_space.canvas:
					Color(0, 1, 0, .2)
					Line(rectangle=[x,y,10,10])
					
		#tool_box.draw(self.tool_box,1)
		

	def load_previous(self):
		tool_box= self.tool_box
		prev = self.prev
		tool_box.draw(self.tool_box,2)


	def saveimage(self):
		ds = self.drawing_space
		save = self.save
		ds.export_to_png('a.png')
