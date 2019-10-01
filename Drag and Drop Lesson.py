from kivy.app import App
from kivy.uix.button import Button

from kivy.core.window import Window
from kivy.uix.behaviors import DragBehavior
from kivy.uix.boxlayout import BoxLayout


class Box_layout(BoxLayout,App):

    def build(self):
        btn=BoxLayout(orientation = "vertical")
        for  x in range(5):
           DragButton.text=str(x)
           btn.add_widget(DragButton())
        return btn


class DragButton(DragBehavior, Button):
    def __init__(self,**kwargs):
       super(DragButton, self).__init__(**kwargs)
       self.drag_rect_width = Window.width
       self.drag_rect_height = Window.height
       self.drag_timeout = 10000000
       self.drag_distance = 10
       self.size_hint=[.1,.1]
       print(Window.height, Window.width)
Box_layout().run()