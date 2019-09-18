from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

class LabellApp(App):


    def build(self):
        w=Window.width
        h=Window.height
        fl=FloatLayout()
        anh1=AnchorLayout(anchor_x='left',anchor_y='top')
        anh2=AnchorLayout(anchor_x='center',anchor_y='top')
        anh3=AnchorLayout(anchor_x='right',anchor_y='top')
        anh4=AnchorLayout(anchor_x='left',anchor_y='center')
        anh5=AnchorLayout(anchor_x='center',anchor_y='center')
        anh6=AnchorLayout(anchor_x='right',anchor_y='center')
        anh7=AnchorLayout(anchor_x='left',anchor_y='bottom')
        anh8=AnchorLayout(anchor_x='center',anchor_y='bottom')
        anh9=AnchorLayout(anchor_x='right',anchor_y='bottom')

        print(w,h)


        label1 = Label(text='[color=FF37F8]TOP[/color][color=64FF5F]-[/color][color=FF2D3E]LEFT[/color]',markup=True,


                       font_size=40,
                       #size=[w,h*.1],
                       #texture_size=[110,91],
                       text_size=[w,h],
                       size_hint=[1,1],
                       valign='top',
                       halign='left')
        anh1.add_widget(label1)

        '''print(Window.width)'''
        label2=Label(text='[color=327AFF]TOP-CENTER[/color]',markup=True,font_size=40,size_hint=[1,1],valign='top',halign='center',text_size=[w,h])
        anh2.add_widget(label2)
        label3=Label(text='[color=531EFF]TOP-RIGHT[/color]',size_hint=[1,1],font_size=40,valign='top',halign='right',text_size=[w,h],markup=True)
        anh3.add_widget(label3)
        label4=Label(text='[color=B74BFF]CENTER-LEFT[/color]',markup=True,font_size=40,size_hint=[1,1],valign='center',halign='left',text_size=[w,h])
        anh4.add_widget(label4)
        label5=Label(text='[color=FF00AE]CENTER-CENTER[/color]',markup=True,font_size=40,size_hint=[1,1],valign='center',halign='center',text_size=[w,h])
        anh5.add_widget(label5)
        label6=Label(text='[color=7AFF6E]CENTER-RIGHT[/color]',markup=True,font_size=40,size_hint=[1,1],valign='center',halign='right',text_size=[w,h])
        anh6.add_widget(label6)
        label7=Label(text='[color=00FFA9]BOTTOM-LEFT[/color]',markup=True,font_size=40,size_hint=[1,1],valign='bottom',halign='left',text_size=[w,h])
        anh7.add_widget(label7)

        label8=Label(text='[color=0A12FF]BOTTOM-CENTER[/color]',markup=True,font_size=40,size_hint=[1,1],valign='bottom',halign='center',text_size=[w,h])
        anh8.add_widget(label8)
        label9=Label(text='[color=DA5549]BOTTOM-RIGHT[/color]',markup=True,font_size=40,size_hint=[1,1],valign='bottom',halign='right',text_size=[w,h])
        anh9.add_widget(label9)
        '''anchor1.add_widget(label1)
        anchor2.add_widget(label2)'''
        #anchor1.add_widget(label1)

        fl.add_widget(anh1)
        fl.add_widget(anh2)
        fl.add_widget(anh3)
        fl.add_widget(anh4)
        fl.add_widget(anh5)
        fl.add_widget(anh6)
        fl.add_widget(anh7)
        fl.add_widget(anh8)
        fl.add_widget(anh9)



        return fl
        #return label1



if __name__ == '__main__':
    LabellApp().run()
