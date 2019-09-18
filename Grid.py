from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class GridLayoutApp(App):
    def build(self):
        btn1=Button(text='Button1',size_hint=[None,None],size=[250,250],background_color=[0,1,0,1])
        grid=GridLayout(cols=3,rows=3,spacing=20)
        for i in range(6):
            grid.add_widget(Button(text='Button'+'{}'.format(i),size_hint=[None,None],size=[250,250],background_color=[0,1,0,1]))
        return grid

if __name__ == '__main__':
    GridLayoutApp().run()
