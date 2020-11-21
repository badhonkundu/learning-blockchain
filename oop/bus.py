from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self):
        super().__init__()
        self.passengers = []


    def add_group(self, passengers):
        self.passengers.extend(passengers)


bus1 = Bus()
bus1.drive()
bus1.add_group(["tata", "mahindra"])
bus1.add_group(["m's"])
print(bus1.passengers)

