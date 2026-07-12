from kivy.app import App
from kivy.uix.label import Label

class GeometryCalculatorApp(App):
    def build(self):
        return Label(text="Geometry Calculator")

GeometryCalculatorApp().run()