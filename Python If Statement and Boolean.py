x_string = input('Enter x coordinate >')
y_string = input('Enter y coordinate >')
x_coord = int(x_string)
y_coord = int(y_string)
 
if y_coord < 0 :
 print('South')
if y_coord > 0 :
 print('North')
if x_coord < 0 :
 print('West')
if x_coord > 0 :
 print('East')
  
  
 x_string = input('Enter x coordinate >')
 y_string = input('Enter y coordinate >')
 x_coord = int(x_string)
 y_coord = int(y_string)
  
 if y_coord < 0 :
  print('South')
 else :
  print('North')

  
 if x_coord < 0 :
  print('West')
 else:
  print('East')
  
  
  x_string = input('Enter x coordinate >')
  y_string = input('Enter y coordinate >')
  x_coord = int(x_string)
  y_coord = int(y_string)
   
  if y_coord < 0 :
   print('South')
  elif y_coord > 0 :
   print('North')
  else:
    print('On x axis')  
 
   
  if x_coord < 0 :
   print('West')
  elif x_coord > 0 :
   print('East')
  else:
    print('On y axis')
   
   
    if 1 == 'one':
	    print('Hello!')
    elif 5 <= cartoon:
	    print("That's all folks!")
  
 
 
 my_string = input('Enter a string >')
 print(my_string)
 my_int = int(input('How many characters are in this string?'))
 print(my_int)
 answer = 'correct'
 if my_int != len(my_string):
  answer = 'incorrect'
 print(answer)
 
 
 a = 1
 b = 2
 c = 5
 d = c // b
 e = c % b
 
 if d > 1 :
  a = b + c
  
 if e > 1:
   a = a + a 
 
 print (a)
  
 
 
 print (7 !='7')
 
 my_string = input('Enter a string >')
 print(my_string)
 my_int = input('How many characters are in this string?')
 print(my_int)
 answer = 'correct'
 if my_int != len(my_string):
   answer = 'incorrect'
 print(answer)
 
 
 #1.
 #Question 1
 #Write a Python program that asks the user to input an integer. If the user enters a non-negative integer, output the factorial of that value. If the user enters a negative integer, don't output anything. 
 
 
from math import factorial
my_int =  int(input('Enter an integer >'))

if my_int > 0 :
 print(factorial(my_int))



 x = 0
 print(x)
 if False:
   x = 2
   print(x)
 elif 'duck' = 'goose':
   x = 4
   print(x)
 else:
   x = 6
   print(x)
 print(x)
 
 
 x = 0
 print(x)
 if False:
   x = 2
   print(x)
 elif 'duck' == 'goose':
   x = 4
   print(x)
 else:
   x = 6
   print(x)
 print(x)
 
 
 
 #Write a Python program that asks the user to input a non-negative integer. If the user enters a non-negative integer, output two times that value. If the user does not enter a non-negative integer, output a warning message.
 
 
 my_int = input('Enter a non-negative integer >')
 
 if my_int.isdigit():
  d_myint=int(my_int)*2
  print(str(my_int) +' * 2 is '+ str(d_myint))  
 else:
   print(my_int+' is not a non-negative integer')
