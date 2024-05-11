from spacetype.room import Room

class Apartment(Room):
    def __init__(self, height, lenght, width, room_num):
        super().__init__(height, lenght, width)
        self.room_num = room_num

    def calc_total_vol(self):
        return self.calc_vol() * self.room_num
    
    def calc_heat_power(self):
        return self.calc_total_vol() * 30