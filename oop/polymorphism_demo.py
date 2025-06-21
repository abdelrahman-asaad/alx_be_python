class Shape:
    def __init__(self):
        pass
    
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()    
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        import math
        return self.radius ** 2 * math.pi    
    
#creating object
shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
    
