# poly ---> many(multiple)
# morph ---> shape

class Animal:
    def __init__(self,name):
        self.name = name

    def make_Sound(self):
        print("The animal making sound")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_Sound(self):
        print("Meow meow")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_Sound(self):
        print("gheu gheu")

class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_Sound(self):
        print("beh beh beh")

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_Sound(self):
        print("KUKKURU KUK")

class Crow(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_Sound(self):
        print("Ka ka ka ka")



don = Cat('Real don')
don.make_Sound()

shepard = Dog("Local Shepard")
shepard.make_Sound()

mess =  Goat("L m")
mess.make_Sound()

chick = Chicken('Chicken')
chick.make_Sound()

kaak = Crow('kaaak')
kaak.make_Sound()

