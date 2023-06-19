#when you declare instance attribute its provide you different cart
#mane duijon shopping korle duita cart ready hobe


class Shop :

    shopping_mall = 'jamuna'
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart =[] #cart is a instance attribute
    def add_to_cart(self,item):
        self.cart.append(item)
    

mehjabeen = Shop('meh jabeen')

mehjabeen.add_to_cart('shoes')
mehjabeen.add_to_cart('mackup')
mehjabeen.add_to_cart('listick')

print(mehjabeen.cart)

nishu = Shop('Nishu')

nishu.add_to_cart('cap')
nishu.add_to_cart('sun glass')
nishu.add_to_cart('mobile')

print(nishu.cart)
