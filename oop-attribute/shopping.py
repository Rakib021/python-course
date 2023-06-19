class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
    def remove_from_cart(self,item):
        for product in self.cart:
            if product['item'] ==item:
                self.cart.remove(product)
                print(f'Removed {item} from the cart')
                return
        print(f'{item} is not found in the cart')
    def checkOut(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        if total <= amount:
            print('Total price:', total)
            print('Change:', amount - total)
        else:
            print('Insufficient amount. Total price:', total)


my_shopping = Shopping('New Market')
my_shopping.add_to_cart('alu', 50, 2)
my_shopping.add_to_cart('piaj', 30, 1)
my_shopping.add_to_cart('tomato', 100, 3)
my_shopping.add_to_cart('kodu', 80, 5)
print(my_shopping.cart)
my_shopping.remove_from_cart('piaj')
my_shopping.checkOut(1600)
