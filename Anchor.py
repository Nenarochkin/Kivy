from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
class AnchorLayoutApp(App):
    def build(self):
        anchor1=AnchorLayout(anchor_x='center',anchor_y='center')
        anchor2=AnchorLayout(anchor_x='left',anchor_y='center')
        btn1=Button(text='Center-center',size_hint=[.3,.3])
        btn2=Button(text='Left-center',size_hint=[.3,.3])
        anchor1.add_widget(btn1)
        anchor2.add_widget(btn2)
        return anchor2
if __name__ == "__main__":

     AnchorLayoutApp().run()
