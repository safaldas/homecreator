import kivy
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.config import Config 

Config.set('graphics','width','1300')
Config.set('graphics','height','700')


Builder.load_file('toolbox.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('generalarea.kv')
Builder.load_file('statusbar.kv')
Builder.load_file('homecreator.kv')



class HomeCreator(BoxLayout):
	pass
class TheHomeCreator(ScreenManager):
	pass
class TheHomeCreatorApp(App):
	def build(self):
		return TheHomeCreator()
if __name__ == "__main__":
	TheHomeCreatorApp().run()