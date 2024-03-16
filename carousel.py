import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.carousel import Carousel


class MyApp(App):

    def build(self):
        carousel=Carousel(direction="top")
        Window.size=[300,600]
        # self.texts= Label(text="hello Developer welcom",on_release=self.submit)
        for i in range(1,4):
            src=f"img/im{i}.jpg"
            image=AsyncImage(source=src)
            carousel.add_widget(image)
        return carousel

        


if __name__=="__main__":
    MyApp().run()        

