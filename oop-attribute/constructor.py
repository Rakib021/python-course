class Phone :
    manufactured ='China'

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

def send_sms(self,phone,sms):
    text = f'sending to : {phone} and message : {sms}'
    print(text)

my_phone = Phone('kala chand','redmi',98000)
print(my_phone.owner,my_phone.brand,my_phone.price)