from kivy.app import App
from kivy.lang import Builder

class GeometryCalculatorApp(App):
    def build(self):
        return Builder.load_file("geometry.kv")

GeometryCalculatorApp().run()