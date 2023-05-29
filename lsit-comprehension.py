numbers =[12,32,65,20,85,95,14,54,33,76,87,51];
odd =[]

for num in numbers:
    if num%2==1:
        odd.append(num)
# print(odd)

odd_num = [num for num in numbers if num %2 ==1 if num %5==0]
# print(odd_num)

players =['sakib','tamim','liton','mushfik']
ages =[38,36,28,32]

palyer_combo =[]
for player in players:
    print('player :',player)
    for age in ages:
        print(player,age)
        palyer_combo.append([player,age])

# print(palyer_combo)

comb2=[[player,age] for player in players for age in ages]
print(comb2)


