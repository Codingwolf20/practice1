import kivy
from kivy.app import App
from kivy.uix import label , boxlayout , button , textinput , checkbox
from kivy.core.window import Window

class MyApp(App):
    def build(self):

        Window.size=[300,600]

        box1 =boxlayout.BoxLayout(orientation="horizontal")
        box2 =boxlayout.BoxLayout(orientation="horizontal")
        box3 =boxlayout.BoxLayout(orientation="horizontal")

        # active =True a of widgets active
        ck1=checkbox. CheckBox(active=True,disabled=True)
        lbl1=label.Label(text="sadegh")
        box1.add_widget(lbl1)
        box1.add_widget(ck1)

        # active =false
        ck2=checkbox. CheckBox()
        lbl2=label.Label(text="tina")
        box2.add_widget(lbl2)
        box2.add_widget(ck2)

        # active =false
        ck3=checkbox. CheckBox()
        lbl3=label.Label(text="farhad")
        box3.add_widget(lbl3)
        box3.add_widget(ck3)

        

        super_box =boxlayout.BoxLayout(orientation= 'vertical')

        super_box.add_widget(box1) 
        super_box.add_widget(box2) 
        super_box.add_widget(box3) 

        return super_box




 
if __name__=="__main__":
     MyApp().run()            
