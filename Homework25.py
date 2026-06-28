class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self):
       
        super().__init__(50)

   
    def fare(self):
        total_fare = super().fare()  
        maintenance_charge = total_fare * 0.10  
        return total_fare + maintenance_charge



school_bus = Bus()


print("Total Bus Fare:", school_bus.fare())