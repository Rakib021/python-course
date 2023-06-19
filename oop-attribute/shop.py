#when you declare class attribute its provide you same cart
#mane duijon shopping korle ekta  cart er moddhe duijon er product ready hobe

class Shop :
    cart =[] #cart is a cart attribute

    def __init__(self,buyer):
        self.buyer =buyer

    def add_to_cart(self,item):
        self.cart.append(item)
    
mehzabeen = Shop('mehzabeen')

mehzabeen.add_to_cart('shoes')
mehzabeen.add_to_cart('face powder')
print(mehzabeen.cart)
