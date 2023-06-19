class Book:
    def __init__(self,name):
        self.name = name

class Physics(Book):
    def __init__(self, name,lab):
        self.lab = lab
        super().__init__(name)

topon = Physics('TOPON', True)
print(issubclass(Physics, Book))