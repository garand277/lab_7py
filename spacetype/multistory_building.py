from spacetype.room import Space

class MultistoryBuilding(Space):
    def __init__(self, height, width, length, num_floors, num_rooms):
        super().__init__(height, length, width)
        self.num_floors = num_floors
        self.num_rooms = num_rooms

    def __str__(self):
        return super().__str__()

    @property
    def calc_vol(self):
        return super().calc_vol() * self.num_rooms * self.num_floors
    
    @property
    def calc_heat_power(self):
        return super().calc_heat_power() * self.num_rooms * self.num_floors