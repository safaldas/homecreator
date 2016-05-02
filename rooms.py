import kivy
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
class room(ScatterLayout,Widget):
	pass

class bedroom(room):
	list_of_size = [(100,100),(140,120)]
	def selectroom(self,typeofroom):
		if typeofroom == 1:
			image_source = "images/bedroom10x10.png"
			return image_source,self.list_of_size[0]
		elif typeofroom == 2:
			return list_of_size[1]

	def draw(self,typeofroom):

		image_source,self.size = self.selectroom(typeofroom)
		with self.canvas:
				Rectangle(source=image_source, pos=self.pos,size= self.size)

