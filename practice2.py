import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class Test(App):
    def build(self):
      
        Window.size=[300,600]
        body =BoxLayout(orientation='vertical')
        
        # ................................................
        titel=Label(text="Developer")
       
        txt =TextInput(multiline=False)
        self.txt=txt
        
        btn =Button(text="[b]SEND[/b]"  ,
        pos_hint={'center_x':0.5,'center_y':0.1} 
        ,size_hint=(0.5,0.2),
        color=(0,1,0.5,1)
        ,font_size="20",background_color=(0,0,1,1)
        ,markup=True)
        # .................on click button action .........................
        btn.bind(on_press=self.press_key)
  
       
        # ..........................................................
        
        body.add_widget(titel)
        body.add_widget(txt)
        body.add_widget(btn)
        # ......................................................
        return body
    def press_key(self,event):
        # print("on click press_key")
        self.txt.text="Thank you:"+self.txt.text
    
        # ........................................

Test().run()
