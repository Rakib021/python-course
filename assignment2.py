N = int(input())
a = list(map(int, input().split()))

count_dict = {}
for x in a:
    count_dict[x] = count_dict.get(x, 0) + 1

removal_count = 0
for x in a:
    if count_dict[x] > x:
        removal_count += count_dict[x] - x
        count_dict[x] = x

print(removal_count)
