#base class,parent class common attribute + functionality class
#derived class ,child class,uncommon attribute + functionality class

class Device :
    def __init__(self,brand,price,color,origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
        self.origin = origin
    def run(self):
         return f'Running Laptop : {self.brand}'



class Laptop:
    def __init__(self,memory,ssd):
       
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f'learning python and practicing'
class Phone(Device):
    def __init__(self,dual_sim,brand,price,color,origin):
       
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
   
    def phone_call(Self,number,text):
        return f'sending sms to : {number} with {text}'
    def __repr__(self):
        return f'phone : {self.brand} and {self.dual_sim}'
class Camera :
    def __init__(self,pixel):
       self.pixel=pixel
    def run(self):
        pass
    def change_lense(self):
        pass
my_phone = Phone('Iphone',12000,'silver','china')
print(my_phone)
