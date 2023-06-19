def call ():
    print("calling someone")
    return 'call done'
class Phone :
    brand='pixel'
    price =120000
    color='white'
    feature =['camera', 'speaker','hamer']

    def call(self):
        print("calling one person")
    def send_Sms (self ,phone,sms):
        text =f'sending sms to {phone} and message : {sms}'
        return text


my_phone = Phone()
print(my_phone.feature)
my_phone.call()
result =my_phone.send_Sms(179344,'i love python')
print(result)
