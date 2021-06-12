class Point3d:
    """тестовый класс для задания"""
    x = 10
    y = 15
    z = 20


p1 = Point3d()
p2 = Point3d()
p3 = Point3d()

print(Point3d.__dict__, p1.__dict__, p2.__dict__, p3.__dict__, sep='\n')
print(Point3d.y, p1.y, p2.y, p3.y)
setattr(Point3d, 'y', 150)
print(Point3d.y, p1.y, p2.y, p3.y)
delattr(Point3d, 'y')
print(getattr(Point3d, 'y', False))
print(getattr(p1, 'y', False))
setattr(p2, 'x', 2)
print(Point3d.x, p1.x, p2.x, p3.x)

