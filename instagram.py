import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.floatlayout  import FloatLayout
from kivy.core.window import Window

class Flatlayout(FloatLayout):

    pass

class Flat(App):
    def build(self):
        Window.size=[300,600]
        return Flatlayout()

if __name__=="__main__":
    Flat().run()        
