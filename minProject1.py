import kivy
from kivy.app import App
from kivy.uix import label , boxlayout , button , textinput
from kivy.core.window import Window


class MyAplicationApp(App):

    def submit(self , e):
        if(self.txt_name.text !="" and self.txt_age.text !="" and self.txt_country.text !=""):

            print(f"{self.txt_name.text} {self.txt_age.text} from {self.txt_country.text}")
            self.btn.disabled=True
            self.btn.text="Thank you"
            self.txt_name.text=""
            self.txt_age.text=""
            self.txt_country.text=""

        else:
            print("Erorr") 

    def build(self):
        Window.size=[300,600]
        self.box=boxlayout.BoxLayout(orientation='vertical')

        self.txt_name=textinput.TextInput(multiline=False)
        self.lbl_name =label.Label(text="please Enter your name")

        self.txt_age=textinput.TextInput(multiline=False)
        self.lbl_age =label.Label(text="please Enter your age")
        
        self.txt_country=textinput.TextInput(multiline=False)
        self.lbl_country =label.Label(text="please Enter your country")

        self.btn=button.Button(background_normal="img/h1.png",background_down="img/h2.png",
        size_hint=(.3,1.2),pos_hint={'x':.35,'y':.0}) 
        self.btn.bind(on_press=self.submit)

        self.box.add_widget(self.lbl_name)
        self.box.add_widget(self.txt_name)

        self.box.add_widget(self.lbl_age)
        self.box.add_widget(self.txt_age)

        self.box.add_widget(self.lbl_country)
        self.box.add_widget(self.txt_country)

        self.box.add_widget(self.btn)


        return self.box
if __name__=="__main__":
    MyAplicationApp().run()        