class University:
    def __init__(self,name,cost,dept):
        self.name = name
        self.cost = cost
        self.dept=dept
    def __repr__(self):
        return f'{self.name} {self.dept}'
    
class canteen(University):
    def __init__(self, name, cost, dept,nasta):
        self.nasta = nasta
        super().__init__(name, cost, dept)
    def __repr__(self):
        return super().__repr__()


campust = canteen('canteen', 12000, 'CSE', 'shingara')
print(campust)
