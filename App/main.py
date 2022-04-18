from kivy.app import App
from kivy.uix.widget import Widget
 
# Test
 
class PongGame(Widget):
    pass
 
 
class PongApp(App):
    def build(self):
        return PongGame()

PongApp() .run()