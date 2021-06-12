from dataclasses import dataclass


@dataclass
class PCPart:
    name: str
    size: tuple = (int, int)


class PersonalComputers:
    def __init__(self, ram_size: int, hdd_size: int, model: str, cpu: str):
        self.__ram_size = ram_size
        self.__hdd_size = hdd_size
        self.__model = model
        self.__cpu = cpu

    def __str__(self):
        return f'Class: {type(self).__name__}\nRam: {self.__ram_size}' \
               f'\nHDD: {self.__hdd_size}\nModel: {self.__model}\nCPU: {self.__cpu}'


class TablePC(PersonalComputers):
    def __init__(self, ram_size: int, hdd_size: int, model: str, cpu: str,
                 monitor: PCPart, keyboard: PCPart, mouse: PCPart):
        super().__init__(ram_size, hdd_size, model, cpu)
        self.__monitor = monitor
        self.__keyboard = keyboard
        self.__mouse = mouse

    def __str__(self):
        result = super().__str__()
        result += f'\nMonitor: {self.__monitor.name} {self.__monitor.size}' \
                  f'\nKeyboard: {self.__keyboard.name} {self.__keyboard.size}' \
                  f'\nMouse: {self.__mouse.name} {self.__mouse.size}'
        return result


class Laptops(PersonalComputers):
    def __init__(self, ram_size: int, hdd_size: int, model: str, cpu: str,
                 display_size: str, size: tuple = (int, int)):
        super().__init__(ram_size, hdd_size, model, cpu)
        self.__display_size = display_size
        self.__size = size

    def __str__(self):
        result = super().__str__()
        result += f'\nSize: {self.__size}\nDisplay size: {self.__display_size}'
        return result


l = Laptops(16, 1024, 'HP Pavilion', 'Intel Core I7 10700', '15.2', (300, 200))
p = TablePC(32, 2048, 'Custom gaming PC', 'AMD Ryzen 7 5800x', PCPart('Asus', (400, 300)),
            PCPart('Genius', (200, 100)), PCPart('Logitech', (100, 80)))
print(p, '\n')
print(l)
