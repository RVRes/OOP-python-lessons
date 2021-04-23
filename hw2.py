class Point3d:
    coords = [10, 20, 30]

    def __init__(self, *args):
        self.coords = [arg for i, arg in enumerate(args) if i < 3]

    def set_coords(self, x=0, y=0, z=0):
        self.coords[0] = x
        self.coords[1] = y
        self.coords[2] = z

    def get_coords(self):
        return tuple(self.coords)


p = Point3d(11, 5, 2, 4, 5, 6, 7, 8)
print(p.get_coords(), type(p.get_coords()), sep='\n')


class Point:
    def __init__(self, x_or_point=0, y=0):
        if isinstance(x_or_point, Point):
            self.x = x_or_point.x
            self.y = x_or_point.y
        else:
            self.x = x_or_point
            self.y = y

    # def __init__(self, *coords, exmp=None):
    #     if coords == ():
    #         self.coords = 0, 0
    #     else:
    #         self.coords = coords
    #
    #     if exmp:
    #         self.coords = exmp.coords


# p1 = Point(456, 456)  # создает с указанными координатами
# p2 = Point(exmp=p1)  # cоздает на основе предыдущего
# p3 = Point()  # создает со значениями по умолчанию (0,0,0)

p1 = Point(5, 10)
p2 = Point(p1)

print(p1.__dict__, type(p1))
print(p2.__dict__, type(p2))
# print(p3.__dict__, type(p3))

pList = []
for i in range(5):
    x, y = map(int, input(f'введите x, y для точки {i}: ').split())
    pList.append(Point(x, y))
for pt in pList:
    print(pt)
