class vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    
class car(vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    def get_info(self):
        return f"{super().get_info()} with {self.num_doors} doors"
    
class electricCar(car):
    def __init__(self, make, model, year, num_doors, battery_size):
        super().__init__(make, model, year, num_doors)
        self.battery_size = battery_size

    def get_info(self):
        return f"{super().get_info()} and a {self.battery_size}-kWh battery"
class hypercar(car):
    def __init__(self, make, model, year, num_doors, top_speed):
        super().__init__(make, model, year, num_doors)
        self.top_speed = top_speed
    
    def get_info(self):
        return f"{super().get_info()} and a top speed of {self.top_speed} mph"
class train(vehicle):
    def __init__(self, make, model, year, num_carriages):
        super().__init__(make, model, year, num_carriages)
        self.num_carriages = num_carriages
    

    def get_info(self):
        return f"{super().get_info()} and a max number of {self.num_carriages} carriages"
    def train_capacity(self):
        capacity = self.num_carriages * 70
        return f"the train capacity is estimated to be around {capacity}"
        



Car1 = electricCar("BYD", "Seal", 2025, 4, 82)


