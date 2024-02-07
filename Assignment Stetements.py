#Assignement Statement
# - used to evaluate an expression and bind an identifier to the result object.
# -bind an identifier to an evaluated expression object

favorite = (input('What is your favorite color?'))
second_favorite = input('What is your second favorite color?')
print("")
print("")

print(favorite)
print('and')
print(second_favorite) 
print('were your picks.')


# rebinding - any identifier can be bound to any oject
# not commendable
#len = id
#print(len('hello')



#my_num = 14
#<st trying to match my_num = 14
  #<as trying to match my_num = 14
    #<ex trying to match 14
    #ex>@li matches 14
  #as>@ex matches 14
#st>@as matches my_num =14


#Question 1
#Write a program that prompts the user to enter an integer and displays the absolute value of that integer on one line and then the original integer on the next line.
integer = (input('Enter an integer > '))
print(abs(int(integer)))
print(integer)
