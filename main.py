from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from formulas import (
    circle_area,
    circle_circumference,
    circle_diameter
)


class HomeScreen(Screen):
    pass


class CalculatorScreen(Screen):
    result = StringProperty("")

    def calculate_area(self):
        try:
            radius = float(self.ids.radius.text)
            self.result = f"Area = {circle_area(radius):.2f}"
        except ValueError:
            self.result = "Enter a valid number."

    def calculate_circumference(self):
        try:
            radius = float(self.ids.radius.text)
            self.result = (
                f"Circumference = {circle_circumference(radius):.2f}"
            )
        except ValueError:
            self.result = "Enter a valid number."

    def calculate_diameter(self):
        try:
            radius = float(self.ids.radius.text)
            self.result = f"Diameter = {circle_diameter(radius):.2f}"
        except ValueError:
            self.result = "Enter a valid number."


class GeometryCalculatorApp(App):
    def build(self):
        return Builder.load_file("geometry.kv")


GeometryCalculatorApp().run()