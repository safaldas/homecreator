from kivy.uix.relativelayout import RelativeLayout

class GeneralArea(RelativeLayout):
	def load_next(self):			
		tool_box= self.tool_box
		next = self.next
		tool_box.draw(self.tool_box,1)

	def load_previous(self):
		tool_box= self.tool_box
		prev = self.prev
		tool_box.draw(self.tool_box,2)


	def saveimage(self):
		ds = self.drawing_space
		save = self.save
		ds.export_to_png('a.png')
		