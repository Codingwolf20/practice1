import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class Test3App(App):
    def build(self):
      
        Window.size=[300,600]
        return  Button(size_hint=(.3,.2),pos_hint={'x':.7,'y':.0},
        background_normal="img/h1.png",background_down="img/h2.png")
     
Test3App().run()
