'hello'[-4]



type('hello'[-3])

cat = "dog"
print(f'hello {cat}')

color = input('What is your favourite color?')
letter = input('What is your favourite letter?')
number_string = input('What is your favourite number?')
number = int(number_string)

if color[number] == letter:
    print('magic')
else:
    print('normal')
    
    
    #Write a Python program that asks the user to input a string that has an e as the middle character. If the string has an odd number of characters and an e as the middle character, output a positive message, as shown in the samples. If the string has an even number of characters or has an odd number of characters, but the middle character is not an e,  output the appropriate negative message as shown in the samples.
    

my_string = input('Enter a string with an e in the middle > ')

str_len = len(my_string)

if str_len%2 == 0:
    print('No, '+ my_string + ' has no middle character')

elif str_len%2 != 0:
    mid = str_len//2
    if my_string[mid ]== 'e':
        print('Yes, ' + my_string + ' has e in the middle, at index ' + str(mid))
    else:
        print('No, ' + my_string + ' has '+  str(my_string[mid ])+' in the middle, at index ' + str(mid))


    