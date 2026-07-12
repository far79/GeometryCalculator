import math

# Circle
def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

def circle_diameter(radius):
    return 2 * radius

# Square
def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side

# Rectangle
def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)