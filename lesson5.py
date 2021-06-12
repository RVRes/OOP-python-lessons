#https://www.youtube.com/watch?v=77kW3F9ZBHI

class Point:
    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Point, cls).__new__(cls)
# здесь ошибка, скорей всего, нужно еще возвращать super(Point, cls).__new__(cls)
        else:
            print('object is already created')

    def __init__(self, x=0, y=0):
        Point.__count += 1
        self.coordX = x
        self.coordY = y

    @staticmethod
    def get_count():
        return Point.__count


pt = Point()
pt2 = Point()
pt3 = Point()
# pt.count = 0
# Point.count = 10
# print(pt.count, pt2.count, pt3.count, sep='\n')
# print(pt.get_count())
print(id(pt), id(pt2), id(pt3), sep='\n')
