colors = ['red','purple','blue','green','yellow','orange']
old_color = input('Enter a color to replace >')
new_color = input('Enter a new color')
if old_color in colors:
    new_index = colors.index(old_color)
    colors[new_index]= new_color
else:
    colors.append(new_color)
print(colors)




#Question 1
#Write a program that uses a list display to create a list containing the integers from 1 to 10 in increasing order, and outputs the list. Then prompt the user to enter a number between 1 and 10, replace this number by the str object gone and output the list. If the user enters a string that does not  represent an integer between 1 and 10, instead output the appropriate message that indicates this situation, as shown in the sample runs:


        
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num_list)
user_input = input('Enter an integer between 1 and 10 > ')

if not user_input.isdigit():
    print(user_input + ' is not a positive integer')
else:
    user_number = int(user_input)

    if user_number in range(1, 11):
        num_list[user_number - 1] = 'gone'
        print(num_list)
    else:
        print(str(user_number) + ' is not between 1 and 10')