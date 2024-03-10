from kivymd.app import MDApp

from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen 
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton 
from kivy.core.window import Window


class MainApp(MDApp):
    def build(self):
            
        self.theme_cls.primary_palette="Yellow"
        # self.theme_cls.theme_style="Dark"
        Window.size=[300,600]
        screen=Screen()
        # ......for button..............................
        icon_btn=MDFloatingActionButton(
            
            icon='plus',
            pos_hint={'center_x':0.8,'center_y':0.1}

            
        )
   

        screen.add_widget(icon_btn) 
        return  screen      
          
      

   
MainApp().run()
