from kivy.app import App
from kivy.properties import ObjectProperty
from navigation_screen_manager import NavigationScreenManager
from canvas_exemples import *


class MyScreenManager(NavigationScreenManager):
    pass

class LeLabApp(App):
    manager = ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        # return CanvasExemples7()

LeLabApp().run()