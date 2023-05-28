balance=500

def buyThings(item,price):
    global balance 
    print("balance inside the function : ", balance)
    balance = balance - price
    print(f'balance after buying {item}',balance)

buyThings('sunglass',200)
print('global balance after buy =',balance)