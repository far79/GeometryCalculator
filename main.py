from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from formulas import circle_area


class HomeScreen(Screen):
    pass


class CalculatorScreen(Screen):
    result = StringProperty("")

    def calculate(self):
        try:
            radius = float(self.ids.radius.text)
            area = circle_area(radius)
            self.result = f"Area = {area:.2f}"
        except ValueError:
            self.result = "Please enter a valid number."


class GeometryCalculatorApp(App):
    def build(self):
        return Builder.load_file("geometry.kv")


GeometryCalculatorApp().run()