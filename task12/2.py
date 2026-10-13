'''Instance methods: Rectangle area and perimeter
Problem: Create a Rectangle class with length and breadth.
 Use instance methods to calculate its area and perimeter.'''

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    
    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)


rect = Rectangle(10, 5)
print(f"Area: {rect.calculate_area()}")
print(f"Perimeter: {rect.calculate_perimeter()}")