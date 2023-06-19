import pyautogui

def draw_pyramid(height):
    screen_width, screen_height = pyautogui.size()
    start_x = screen_width // 2
    start_y = screen_height // 2
    
    for i in range(height):
        num_blocks = i * 2 + 1
        start_x -= num_blocks // 2
        
        for j in range(num_blocks):
            pyautogui.click(start_x + j, start_y + i)
    
        start_x += num_blocks // 2

# Prompt the user to enter the height of the pyramid
height = int(input("Enter the height of the pyramid: "))

# Call the function to draw the pyramid
draw_pyramid(height)
