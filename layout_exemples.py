from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_file("layout_exemples.kv")

class MainWidget(Widget):
    pass


class AnchorLayoutExemple(AnchorLayout):
    pass


class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation= "lr-bt"
        for i in range(0, 100):
            b = Button(text =str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)

class GridLayoutExemple(GridLayout):
    pass


class BoxLayoutExemple(BoxLayout):
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""

