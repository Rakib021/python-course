class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f'{self.name} {self.price}'

    def move(self):
        pass

class Bus(Vehicle):
     def __init__(self, name, price,seat):
        self.seat = seat
        super().__init__(name,price)

     def __repr__(self):
        return super().__repr__() 

class Truck(Vehicle):
    def __init__(self, name, price,weight):
        self.weight = weight
        super().__init__(name, price)
class pickup(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)
class AcBus(Bus):
    def __init__(self, name, price, seat):
        super().__init__(name, price, seat)

    def __repr__(self):
        return super().__repr__()

ac_bus = AcBus('greenLine', 500000000, 22)
print(ac_bus)