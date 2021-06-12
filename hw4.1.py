class CoordsDescriptor:
    def __set_name__(self, owner, name):
        self.__name = '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value: tuple = (0, 0)):
        if isinstance(value, tuple) and len(value) == 2:
            instance.__dict__[self.__name] = value
        else:
            raise ValueError('проверьте ввод даннхы (x,y)')


class Rectangle:
    top_left = CoordsDescriptor()
    bottom_right = CoordsDescriptor()

    def __init__(self, topleftX: int = 0, topleftY: int = 0, bottomrightX: int = 0, bottomrightY: int = 0):
        self.top_left = topleftX, topleftY
        self.bottom_right = bottomrightX, bottomrightY

    def __str__(self):
        return 'Rectangle(top_left(x={},y={}),bottom_right(x={},y={})'.format(self.top_left[0],
                                                                              self.top_left[1],
                                                                              self.bottom_right[0],
                                                                              self.bottom_right[1])


print()
print('-' * 100)
rec = Rectangle()
print(rec, rec.__dir__(), rec.__dict__, sep='\n')
print('-' * 100)

rec.bottom_right = 1, 5
print(rec, rec.__dir__(), rec.__dict__, sep='\n')
print(rec.bottom_right, type(rec.bottom_right))
print(rec.top_left, type(rec.top_left))

print('-' * 100)
rec2 = Rectangle(1, 2, 3, 4)
print(rec2, rec2.__dict__)
