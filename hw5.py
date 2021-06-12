class Rectangle:

    def __init__(self, lenght: int = 0, height: int = 0):
        self.area = Rectangle.calc_rectangle_area(lenght, height)

    @staticmethod
    def calc_rectangle_area(x, y: int = 0):
        return x * y


rec = Rectangle(10, 20)
print(rec.__dict__)