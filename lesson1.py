#https://www.youtube.com/watch?v=Yt08fz52Cj0&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B

class Point:
    """Класс точка для тестирования ООП"""
    x = 5
    y = 9


pt = Point()
pt.x = 100

print(pt.__dir__)
print(Point.__dir__)
print(pt.__dict__)
print(Point.__dict__)
print(Point.__name__)
print(Point.__doc__)
print(pt.__doc__)
print('-'*100)
print(getattr(pt, 'x'))
# print(getattr(pt, 'z'))
print(getattr(pt, 'z', False))
setattr(pt, 'z', 7)
print(pt.__dict__)
pt.__delattr__('z')
print(pt.__dict__)
print('-'*100)
print(isinstance(pt, Point))
