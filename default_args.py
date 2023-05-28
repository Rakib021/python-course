def allSum(*numbers):
    sum =0
    for num in numbers:
        print(num)
        sum = sum+num
    return sum


total = allSum(54,23,21,43,25)
print("total sum : ", total)