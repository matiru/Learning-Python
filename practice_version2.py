#Question 7
#Write a program that uses the uagame module to open a 300 by 200 pixel window with title, hello.  Prompt the user to enter a string using the prompt string 'Enter string >'. The prompt must be in the top left corner of the window. Then, display the input string in the bottom right hand corner of  the window. This program must work for any reasonable font size, so your program must use the Window methods named: get_width, get_string_width, get_height, and get_font_height to compute the display_string coordinates for displaying the string in the bottom right corner. The program should pause for 2 seconds after the string appears in the window and then the window should close. Your program must not input or display any other information.


from uagame import Window
from time import sleep
#create window

window = Window('hello',1300,700)
window.set_font_name('')
window.set_font_size(22)
window.set_font_color('red')
window.set_bg_color('black')

# display content
line_y = 0 
user_str = window.input_string('Enter string>',0,line_y)
print(type(user_str))

x=window.get_width()-window.get_string_width(user_str)
y=window.get_height() - window.get_font_height()
window.draw_string(user_str,x,y)
window.update()

sleep(2)
window.close()