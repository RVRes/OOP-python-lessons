class Descriptors:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __delete__(self, instance):
        # print('deleting: ' + self.__name)
        del instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Point:
    coordX = Descriptors()
    coordY = Descriptors()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


p = Point()
print(p.__dir__(), p.__dict__, sep='\n')
print(p.coordX, p.coordY)
p.coordY = 100
print(p.coordX, p.coordY)
del p.coordY
print('-' * 100)
print(p.__dir__(), p.__dict__, sep='\n')
