#encaptulation ===> hide details
#access modifier ===> public,private,protected

class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name = holder_name #public attribute
        self.initial_deposit = initial_deposit 
        self.__balance = initial_deposit #private attribute
        self._branch ="kathgor" #protected attribute
    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        if amount <self.__balance:
            self.__balance = self.__balance -amount
            return amount
        else:
            return f'fokira taka nai'
    def get_balance(self):
        return self.__balance



raafsun =Bank('chooto', 1000)

# print(raafsun.holder_name)
raafsun.deposit(40000)
print(raafsun.get_balance())
print(raafsun._branch)
# print(dir(raafsun))
print(raafsun._Bank__balance)