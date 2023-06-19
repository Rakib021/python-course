class Three_instance:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c=c
    
    def sum(self):
        return self.a +self.b+self.c
    def factorial(self):
        fact =1

        for num in range(1,self.b+1):
            fact *=num
        return fact

factt = Three_instance(13,5,21)
print("factorial =", factt.factorial())
print("sum = ",factt.sum())
