#tuple
'Kiwi','Orange',27,len

# parenthesized expression

()
(3+4)*5

#list

["Kiwi",'orange',23,len]


colors = ('white', 'red', 'blue', 'yellow')
mixed_colors = ['white', 'red', 'purple', 'orange', 'blue', 'white', 'green', 'white', 'white', 'yellow']
first_color = input('Enter one of: ' + str(colors))
second_color = input('Enter one of: ' + str(colors))
first_index = colors.index(first_color)
second_index = colors.index(second_color)
if first_index == 0:
  mix_index = second_index*second_index
elif second_index == 0:
  mix_index = first_index*first_index
else:
  mix_index = first_index*second_index
mix_color = mixed_colors[mix_index]
print(first_color, '+', second_color, '=', mix_color)

#Question 1
#Write a Python program that creates an empty list and an empty tuple and then outputs them as shown in the sample run. The program must then input a string, use the append method to append the str object to the empty list and output the list. The program must then create a tuple that contains the same str object and output the tuple.


my_list =[]
my_tuple = ()

my_string = input('Enter a string >')

my_list.append(my_string)
my_tuple = (str(my_string),)

print(my_list)
print(my_tuple)


#correct answers

print([])
print(())
my_string = input('Enter a string >')
print([my_string])
print(tuple([my_string]))


my_list =[]
my_tuple = ()

my_string = input('Enter a string >')

my_list.append(my_string)
my_tuple = tuple(my_list)

print(my_list)
print(my_tuple)