class Point3d:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self):
        return f'{type(self).__name__} (x: {self.__x}, y: {self.__y}, z: {self.__z})'

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f'{self.__class__.__name__} expected')
        return Point3d(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f'{self.__class__.__name__} expected')
        return Point3d(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    def __mul__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f'{self.__class__.__name__} expected')
        return Point3d(self.__x * other.__x, self.__y * other.__y, self.__z * other.__z)

    def __truediv__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f'{self.__class__.__name__} expected')
        return Point3d(self.__x // other.__x, self.__y // other.__y, self.__z // other.__z)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise TypeError('Key as string expected')
        if item == 'x':
            return self.__x
        elif item == 'y':
            return self.__y
        elif item == 'z':
            return self.__z

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('Key as string expected')
        if not isinstance(value, int):
            raise TypeError('Value as integer expected')
        if key == 'x':
            self.__x = value
        elif key == 'y':
            self.__y = value
        elif key == 'z':
            self.__z = value



p1 = Point3d(10, 20, 30)
p2 = Point3d(1, 2, 3)
p3 = p1 + p2
print(p3)
print(p3['x'], p3['y'], p3['z'])
