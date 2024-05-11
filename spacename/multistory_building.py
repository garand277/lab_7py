from spacetype import Apartment

class MultistoryBuilding(Apartment):
    def __init__(self, height, width, length, num_floors, num_rooms):
        super().__init__(height, length, width, num_rooms)
        self.num_floors = num_floors

    def calc_total_vol(self):
        return super().calc_total_vol() * self.num_floors
    
    def calc_heat_power(self):
        return self.calc_total_vol() * 30.2