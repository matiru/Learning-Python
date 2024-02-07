 from time import sleep,asctime
 now = asctime()
 print('The current time is ' + now)
 sleep(12)
 print('goodbye')
 
 int = 3 
 print(int) 


 your_string = input('Enter a number >')
 your_int = int(your_string)
 your_sqrt = sqrt(your_int)
 print(your_sqrt)
 
 
 from math 'import' sqrt
 your_string = input('Enter a number >')
 your_int = int(your_string)
 your_sqrt = sqrt(your_int)
 print(your_sqrt)
 
 from math import sqrt, degrees, exp, gamma
 your_string = input('Enter a number >')
 your_int = int(your_string)
 your_sqrt = sqrt(your_int)
 print(your_sqrt)
 
 
 from math import sqrt,
 your_string = input('Enter a number >')
 your_int = int(your_string)
 your_sqrt = sqrt(your_int)
 print(your_sqrt) 
 
 import math sqrt
 your_string = input('Enter a number >')
 print(your_string)
 your_int = int(your_string)
 your_sqrt = sqrt(your_int)
 print(your_sqrt)
 
 
 #Question 1
 #Write a program that prompts the user to enter a number of degrees. The program should then use the sin function from the math library to compute and display the sin of the angle. Since the sin function expects its argument to be an angle in radians instead of degrees you must convert from degrees to radians before calling the sin function. Look in the math module for a function that converts an angle from degrees to radians and import and use that function as well. 
 
from math import sin,degrees,radians

angle = float(input('Enter an angle value in degrees >'))
angle_degree =(int(angle))
print(angle_degree)
angle_radian = radians(angle_degree)
print(angle_radian)
angle_sin = sin(angle_radian)
print(angle_sin)

print('The sin of ' + str(angle) + ' degrees is ' + str(angle_sin))

              