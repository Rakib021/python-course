class Book:
    author ='Rakibul islam'

    def info():
        print("this book is writen by Rakibul islam")
    def __init__(self,name,price):
        self.name = name
        self.price =price
my_book = Book('Rakibul islam',1200)
print(my_book.name,my_book.price)