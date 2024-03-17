import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout  import GridLayout
from kivy.core.window import Window




test =Builder.load_string("""
# Label:
#     text: "developer"
#     font_size: '20'
#     markup:True
#     color: 1 , 1, 0
    
""")
class MainLayout(GridLayout):
    pass

class Tesst(App):
    def build(self):
        Window.size=[300,600]
        return MainLayout()



if __name__=="__main__":
    Tesst().run()        
