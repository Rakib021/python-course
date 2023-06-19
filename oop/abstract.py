from abc import ABC, abstractmethod
#abstract base class



class Animal(ABC):
    @abstractmethod #inforce all derived class to have a eat method
    def eat(self):
        print("hey nana i am eating banana")
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name):
        self.category ='Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print("hey na ana nana i am eating bananan")
        


layka= Monkey('Lucky')

print(layka.eat())