from kivy.app import App
from kivy.uix.widget import Widget

class RetrackInicio(Widget):
    pass

class RetrackApp(App):
    def build(self):
        return RetrackInicio()
        
if __name__ == '__main__':
    RetrackApp().run()