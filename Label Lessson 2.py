from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
class LabelApp(App):
    def build(self):
        print(Window.width)

        w=Window.width*0.1
        h=Window.height*0.1
        print(w,'w',h,'h')



        label=Label(text="""[size=12][color=32B0FF] Some text[/color] [/size]
                             """ ,
                           markup=True,
                           size_hint=[None,None],
                           size=[w,h],
                           text_size=[w,h],
                           valign='center',
                           halign='right',

                                )

        return label

LabelApp().run()