from abc import ABC, abstractmethod
class Space(ABC):
    @abstractmethod
    def __init__(self, height, wight, lenght):
        self.height = height
        self.wight = wight
        self.lenght = lenght
    @abstractmethod
    def calc_vol(self):
        return self.height * self.lenght * self.wight

    @abstractmethod
    def calc_heat_power(self):
        return self.height * self.lenght * self.wight * 0.03


class Room(Space):
    def __init__(self, height, wight, lenght):
        super().__init__(height, wight, lenght)

    def calc_vol(self):
        return super().calc_vol()
    
    def calc_heat_power(self):
        return super().calc_heat_power()