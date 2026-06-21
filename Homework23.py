import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

        def area(self):
            return 2 * math.pi * self.radius ** 2
        def perimeter(self):
            return 2 * math.pi * self.radius



radius = float(input("Enter the radius :"))


circle = Circle(radius)


print("area:", circle.area())
print("Perimeter (Circumference):", circle.perimeter)