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

    def open_calculator(self, shape):
        calculator = self.manager.get_screen("calculator")
        calculator.set_shape(shape)
        self.manager.current = "calculator"


class CalculatorScreen(Screen):
    title = StringProperty("Calculator")
    result = StringProperty("")

    def set_shape(self, shape):
        self.title = f"{shape} Calculator"

    def get_radius(self):
        text = self.ids.radius.text.strip()

        if not text:
            self.result = "Please enter a radius."
            return None

        try:
            radius = float(text)
        except ValueError:
            self.result = "Enter a valid number."
            return None

        if radius <= 0:
            self.result = "Radius must be greater than 0."
            return None

        return radius

    def calculate_area(self):
        radius = self.get_radius()
        if radius is None:
            return

        self.result = f"Area = {circle_area(radius):.2f}"

    def calculate_circumference(self):
        radius = self.get_radius()
        if radius is None:
            return

        self.result = f"Circumference = {circle_circumference(radius):.2f}"

    def calculate_diameter(self):
        radius = self.get_radius()
        if radius is None:
            return

        self.result = f"Diameter = {circle_diameter(radius):.2f}"


class GeometryCalculatorApp(App):
    def build(self):
        return Builder.load_file("geometry.kv")


GeometryCalculatorApp().run()