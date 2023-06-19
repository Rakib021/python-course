class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw =100000

    def get_balance (self):
        return self.balance;
    def deposit(self,amount):
        if amount >  0:
            self.balance +=amount
            return f'here is your deposited money {amount}'
    def withdraw(self,amount):
        if  amount <self.min_withdraw:
            return f'you can not withdraw below {self.min_withdraw}'
        elif amount > self.max_withdraw:
            return f'You cannot withdraw more then {self.max_withdraw}'
        
        else:
            self.balance -= amount
            return f'here is your money {amount}'


brac= Bank(15000)


# print(brac.withdraw(2500))
# print(brac.get_balance())

print(brac.deposit(1300))
print(brac.get_balance())

