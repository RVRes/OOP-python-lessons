class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkvalue(x):
        return True if isinstance(x, int) or isinstance(x, float) else False

    def __set_coordsX(self, x):
        if Point.__checkvalue(x):
            self.__x = x
        else:
            raise ValueError('wrong data format')

    def __get_coordsX(self):
        return self.__x

    def __del_coordsX(self):
        print('del X')
        del self.__x

    @property
    def coordY(self):
        return self.__y


    @coordY.setter
    def coordY(self, y):
        if Point.__checkvalue(y):
            self.__y = y
        else:
            raise ValueError('wrong data format')

    @coordY.deleter
    def coordY(self):
        print('del Y')
        del self.__y

    coordX = property(__get_coordsX, __set_coordsX, __del_coordsX)


p = Point(3, 4)

p.coordX = 100
print(p.coordX)
# p.coordX = '100'
p.coordY = 1010
print(p.coordY)

del p.coordX
