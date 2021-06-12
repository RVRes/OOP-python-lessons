# task 1
import datetime


class Calendar(object):
    # __date: datetime.date
    __slots__ = ['__date', '__dict__']

    def __init__(self, date: datetime.date = None):
        self.date = date
        pass

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: datetime.date):
        self.__date = date

    @date.deleter
    def date(self):
        del self.__date


d = Calendar()
print(d, d.__dir__(), d.__dict__, sep='\n')

d.date = datetime.date.today()
print(d, d.__dict__, d.date, type(d.date), sep='\n')
print(d._Calendar__date)

print('-' * 100)
