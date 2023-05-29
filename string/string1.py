import turtle

name = turtle.textinput("name", "what is your name?")
name= name.lower()
if name.startswith("mr"):
    print("Hello sir how are you?")
elif name.startswith("mrs"):
    print("Hello madam how are you?")
else:
    name= name.capitalize()
    str="hi" + name +"! how are you?"
    print(str)

turtle.exitonclick()