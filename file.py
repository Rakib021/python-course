#.csv ==> comma separated file
#.txt ==>text

# with open('message.txt' ,'w') as file:
#     file.write("I love you ,python")
# with open("message.txt",'a') as file:
#       file.write("Mohammed Rakib")

with open("message.txt",'r') as file:
   text=file.read()
   print(text)