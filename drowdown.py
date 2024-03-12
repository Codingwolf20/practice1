import kivy
from kivy.app import App
from kivy.uix import label , boxlayout , button , textinput , checkbox 
from kivy.uix.dropdown  import DropDown
from kivy.core.window import Window

class MyDropDownApp(App):
    def build(self):
        Window.size=[300,600]
        dropdown =DropDown()

        for item in range(5):
            btn= button.Button(text=f"Button {item}",size_hint_y=None,height=30)
            btn.bind(on_release=lambda btn :dropdown.select(btn.text))
            dropdown.add_widget(btn)


        superbtn=button.Button(text="drop down",size_hint=(.3,.1),pos_hint={'x':.35,'y':.45})
        superbtn.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance ,text :setattr(superbtn,"text" ,text))
        return superbtn



if __name__=="__main__":
    MyDropDownApp().run()
