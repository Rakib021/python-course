numbers=[12,32,43,5,4,65,23];
numbers.append(89)
numbers.insert(3, 30)
if 43 in numbers:
    numbers.remove(43)
if 3 in numbers: 
    numbers.remove(3)
print(numbers)
last = numbers.pop()
print(numbers)
sorted = numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
index=numbers.index(23)
print(index)