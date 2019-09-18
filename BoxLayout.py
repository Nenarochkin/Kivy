from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxApp(App):
    def build(self):
        box=BoxLayout(orientation='horizontal',padding=[50,50,50,50],spacing=20)
        box.add_widget(Button(text='button1'))
        box.add_widget(Button(text='button2'))
        box.add_widget(Button(text='button3'))
        return box

if __name__ == '__main__':
    BoxApp().run()
