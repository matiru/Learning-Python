#Question 1
#Write a Python program that asks the user to input an integer. If the user enters an integer, output the negative of that integer. If the user does not enter an integer, output a warning message. For this question a valid integer consists of one or more digits (0-9) with an optional leading minus sign 



  
my_int =  input('Enter an integer >') 

if my_int.lstrip('-').isdigit():
 n_myint = -int(my_int)
 print('The negative of '+ my_int + ' is '+ str(n_myint)) 
else:
 print(my_int+' is not an integer')
 

