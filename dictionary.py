person ={'name ': 'Rakib', 'address':'chittagong', 'age':23,'job':'student'}
print(person['job'])
print(person.keys())

person['language'] ='python'

print(person)

#special dictionary looping

for key,value in person.items():
    print(key,value)