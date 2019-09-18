from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics','resizable','0')
Config.set('graphics','width','800')
Config.set('graphics','height','400')


class Mybtn(App):
    def build(self):


        return Button(text= "Hello",
                      background_color=[1,0,0,1],
                      background_normal='0.jpg',
                      font_size=40,
                      background_down='0.jpg',
                      size_hint=[None,None],
                      size=[250,250],
                      pos=[250,50],
                      border=[2,2,2,2],
                      on_press=self.Click )
    def Click(self,instance):
         instance.text='Hi'
         instance.background_normal='1.jpg'



if __name__ == '__main__':
    Mybtn().run()
