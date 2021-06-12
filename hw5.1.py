class Dog:
    __count = 0

    def __init__(self):
        Dog.__count += 1
        self.name = None
        self.age = None
        self.type = None

    def __new__(cls, *args, **kwargs):
        if Dog.__count < 5:
            return super().__new__(Dog)
        else:
            print('Instances more than 5')

    def __del__(self):
        Dog.__count -= 1

    @staticmethod
    def get_count():
        return f'Создано {Dog.__count} экземпляров'


d1 = Dog()
d2 = Dog()
d3 = Dog()
d4 = Dog()
d5 = Dog()
d6 = Dog()
d7 = Dog()

print(id(d1), id(d2), id(d3), id(d4), id(d5), id(d6), id(d7), sep='\n')
print(type(d1), type(d6), sep='\n')
print(Dog.get_count())