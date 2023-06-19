class Calculator :
    brand ='casio es100'
    def add(self,num1,num2):
        return num1+num2
    def deduct (self,num1,num2):
        return num1-num2
    def multiply(self,num1,num2):
            return num1*num2
    def divide (self,num1,num2):
        return num1 /num2

calc = Calculator()

print(calc.brand)
print("sum =",calc.add(10, 30))
print("deduction = ", calc.deduct(70, 45))
print("multiplication = ", calc.multiply(23,6))
print("Divide = ", calc.divide(70, 45))

