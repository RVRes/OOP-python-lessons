# https://www.youtube.com/watch?v=7kk2gRf8Uws&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B

# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.a = x
#         self.b = y
#
#
# pt = Point()
# # pt.set_coords(5, 10)
# Point.set_coords(pt, 5, 10)
# print(pt.__dict__)

class Point:
    x = 1
    y = 1

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print('удаляем экземпляр класса', self.__str__())


pt1 = Point()
pt2 = Point(5)
pt3 = Point(5, 10)
print(pt1.__dict__, pt2.__dict__, pt3.__dict__, sep='\n')
