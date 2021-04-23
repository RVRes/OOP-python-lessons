# https://www.youtube.com/watch?v=WP2sqI2BkeY&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=3

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#
# p = Point(5, 10)
# print(p.x, p.y)
# p.x = 100
# p.y = 'abc'
# print(p.x, p.y)

class Point:
    WIDTH = 5
    # __slots__ = ['__x', '__y']

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkvalue(x):
        return True if isinstance(x, int) or isinstance(x, float) else False

    def render(self):
        print(self.__x, self.__y)

    def set_coords(self, x, y):
        if Point.__checkvalue(x) and Point.__checkvalue(y):
            self.__x = x
            self.__y = y
        else:
            print('значения должны быть числами')

    def get_coords(self):
        return self.__x, self.__y

    def __getattribute__(self, item):
        if item == '_Point__x':
            return 'частная переменная'
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'WIDTH':
            raise AttributeError
        else:
            self.__dict__[key] = value


p = Point(5, 10)
# print(p.__x, p.__y)
setattr(p, '__x', 0)
print(p.__dict__)
p.render()
p.set_coords('11', 6)
p.render()
print(p.get_coords())
print(p._Point__x)
