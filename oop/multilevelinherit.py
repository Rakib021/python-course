class Vehicle:
     def __init__(self,name,types):
        self.name = name
        self.types = types
     def __repr__(self,name,types):
        return f'{self.name} {self.types}'

class Bus(Vehicle):
    def __init__(self,name,seat,types):
        self.seat = seat
        super().__init__(name,types)
    def __repr__(self):
        return super().__repr__(self.name,self.types)

class AcBus(Bus):
    def __init__(self,name,price,seat,types):
        self.price = price
        super().__init__(name,seat,types)
    def __repr__(self):
        return super().__repr__()

bus1 = AcBus('Soudia',800,24,'Ac')
print(bus1)
