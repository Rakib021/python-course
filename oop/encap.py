class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("Animal making sound")
    
class Dog(Animal):
    def __init__(self,name):
        self.name = name
        super().__init__(name)
    def sound(self):
        print("Gheu Gheu")
class Cat(Animal):
    def __init__(self,name):
        self.name = name
        super().__init__(name)
    def sound(self):
        print("Meow meow")

animal1 = Dog('Shepard')
animal1.sound()
animal2 = Cat('meowwwwwwwww')
animal2.sound()