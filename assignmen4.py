n = int(input())
numbers = list(map(int, input().split()))


all_even = all(num % 2 == 0 for num in numbers)

if all_even:
    operations = 0
    while all_even:
        numbers = [num // 2 for num in numbers]
        all_even = all(num % 2 == 0 for num in numbers)
        operations += 1

    print(operations)
else:
    print(0)  
