import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.floatlayout  import FloatLayout
from kivy.core.window import Window

# class Flatlayout(FloatLayout):

#     pass
class MyGridlayout(GridLayout):
    def calc (self,event):
        if event: #3/0
            try:
                self.display.text= str(eval(event))
            except:
                self.display.text="erorr"     
        
class Developer(App):

    def build(self):
        Window.size=[300,600]
        
        return MyGridlayout()


if __name__=="__main__":
    Developer().run()        
