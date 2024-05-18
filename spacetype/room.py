from abc import ABC, abstractmethod
class Space(ABC):
    @abstractmethod
    def __init__(self, height, width, lenght):
        self.height = height
        self.width = width
        self.lenght = lenght

    @abstractmethod
    def calc_vol(self):
        return self.height * self.lenght * self.width

    @abstractmethod
    def calc_heat_power(self):
        return round(self.height * self.lenght * self.width * 0.03, 2)
    
    @abstractmethod
    def __str__(self):
        return f"Общий объем: {self.calc_vol()} куб.м\nТепловая мощность: {self.calc_heat_power()} кВт"

class Room(Space):
    def __init__(self, height, width, lenght):
        super().__init__(height, width, lenght)

    def __str__(self):
        return super().__str__()

    def calc_vol(self):
        return super().calc_vol()
    
    def calc_heat_power(self):
        return super().calc_heat_power()