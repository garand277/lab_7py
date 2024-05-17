from spacetype.room import Space

class Apartment(Space):
    def __init__(self, height, wight, lenght, room_num):
        super().__init__(height, wight, lenght)
        self.room_num = room_num

    def calc_vol(self):
        return super().calc_vol() * self.room_num
    
    def calc_heat_power(self):
        return super().calc_heat_power() * self.room_num