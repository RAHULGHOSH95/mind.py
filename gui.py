import kivy
kivy.require('1.0.8')

from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.uix.listview import ListView
from kivy.base import runTouchApp
from kivy.config import Config 


class MainView(ListView):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(

def on_enter(instance, value):
    print('User pressed enter in', instance)

    class BTNTEXTApp(App):  
        def build(self):
             b = BoxLayout(orientation ='vertical', )
              t = TextInput()

              f = Button()
               def register(self):
        print("user: ", self.ids.user_input.text)
        b.add_widget(t)  
        b.add_widget(f) 

if __name__ == '__main__':
    MyApp().run()
