# class Nvidia:
#     pass
#
#
# class GeForce:
#     pass
#
#
# class AMD:
#     pass
#
#
# class Intel:
#     pass
#
#
# class CPU(AMD, Intel):
#     def __init__(self, name, *args):
#         super().__init__(name, *args)
#         self.__name = name
#
#     def __str__(self):
#         return f'{type(self).__name__}: {super().__str__()}\n{self.__name}'
#
#
# class GPU(Nvidia, GeForce):
#     def __init__(self, name, *args):
#         super().__init__(name, *args)
#         self.__name = name
#
#     def __str__(self):
#         return f'{type(self).__name__}: {super().__str__()}\n{self.__name}'
#
#
# class Memory:
#     def __init__(self, name, *args):
#         super().__init__(*args)
#         self.__name = name
#
#     def __str__(self):
#         return f'{type(self).__name__}: {super().__str__()}\n{self.__name}'
#
#
# class Motherboard(CPU, GPU, Memory):
#     pass
#
#     def __init__(self, name, *args):
#         self.__name = name
#         super().__init__(*args)
#
#
#     def __str__(self):
#         return f'{type(self).__name__}: {super().__str__()}\n{self.__name}'
#
#
# m = Motherboard('asus_motherboard', 'cpu_intel', 'Nvidia_gpu', 'kingston_memory')
# print(m)


class Cpu_Values:
    '''CPU models collections united by the brand names'''
    la = ['Ryzen 5 3400G', 'Ryzen Threadripper', 'Ryzen 3 3100']
    li = ['Core i5-8400', 'Core i9-10900K', 'Xeon E5-2697V3']


class Ram:
    """RAM capacity"""

    def ram_info(self, value: str):
        return f"Amount of RAM {value} "


class Amd:
    """AMD CPU data"""

    def amd_info(self, mod: Cpu_Values, cores: int, threads: int):
        return f'''CPU installed is AMD:
{mod}, {cores} cores/ {threads} threads'''


class Intel:
    """Intel CPU data
    Имеет дополнительное свойство, которого нет
    в классе Amd """

    def intel_info(self, mod: Cpu_Values, cores: int, threads: int, add: str = ' --'):
        return f'''CPU installed is Intel: 
{mod}, {cores} cores/ {threads} threads, 
additional data: {add}'''


class Nvidia:
    """Nvidia GPU data"""

    def nvidia_info(self):
        return 'GPU installed is Nvidia'


class Geforce:
    """GeForce GPU data"""

    def geforce_info(self):
        return 'GPU installed is Geforce'


class Cpu(Amd, Intel):
    """CPU configuration
    Вспомогательный класс. Экземпляров не создает.
    Проверяет наличие брендов CPU и обеспечивает вывод
    их характеристик в консоль
    """

    def __init__(self):
        super().__init__()

    def cpu_info(self, *cval):
        """Configure CPU brand, model, cores information
        *cval позволяет принимать разные свойства и разное
        количество свойств из классов Amd и Intel
        """
        if self.cpu == 'AMD':
            return self.amd_info(*cval)  # вызываем метод из класса Amd
            # без упоминания самого класса Amd, просто через self
        elif self.cpu == 'Intel':
            return self.intel_info(*cval)  # то же самое с методом класса Intel
        else:
            raise ValueError("не предусмотренный тип CPU")


class Gpu(Nvidia, Geforce):
    """GPU configuration"""

    def __init__(self):
        super().__init__()

    def gpu_info(self):
        """Configure GPU brand and model information"""
        if self.gpu == 'Nvidia':
            return self.nvidia_info()
        elif self.gpu == 'Geforce':
            return self.geforce_info()
        else:
            raise ValueError("не предусмотренный тип GPU")


class Motherboard(Cpu, Gpu, Ram):
    """Uniting the CPU, GPU and RAM information
    Множественное наследование, не зависящее, в каком порядке
    переданы названия родительских классов: можно поменять
    местами (Ram, Cpu, Gpu)
    """

    def __init__(self, cpu, gpu, ram: str, *cval):
        super().__init__()
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.cval = [el for el in cval]

    def motherboard_info(self):
        return f'''{self.cpu_info(*self.cval)}, 
{self.gpu_info()},
{self.ram_info(self.ram)}'''


# ПРОВЕРКИ
mob = Motherboard('AMD', 'Geforce', '64 Gb', Cpu_Values().la[1], 8, 16)
print(mob.motherboard_info())
print()
mob2 = Motherboard('Intel', 'Nvidia', '192 Gb', Cpu_Values().li[2], 14, 28)
print(mob2.motherboard_info())
print()
mob3 = Motherboard('Intel', 'Geforce', '128 Gb', Cpu_Values().li[0], 6, 6, '! HELLO!')
print(mob3.motherboard_info())