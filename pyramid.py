import pyAutogui

def print_pyramid():
    rows=int(input())
    for i in range(1, rows + 1):
        print("*" * i)
        
pyAutogui.press(print_pyramid())

