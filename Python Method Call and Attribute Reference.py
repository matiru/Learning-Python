print('hello goodbye'.upper().isupper())

print('hello goodbye'.upper().find('G'))

print('helo goodbye'.upper().find('G'))

print(len('hello goodbye').upper())

print('hello'.upper.lower())

x = 'purple'
y = x.isupper
z = type(y)
print(x)
print(y)
print(z)

word_1 = 'double quotes'
my_string = 'I am using "' + word_1 + '".'
print(my_string)

#Question 1
#Write a Python program that asks the user to input a string and a sub-string and outputs the number of occurrences of the sub-string in the string.

str1 = input('Enter a string >')
sub_str1 = input('Enter a substring >')
count = str1.count(sub_str1)
print('the substring "'+sub_str1+'" appears '+ str(count)+' times in "'+str1 +'"')



