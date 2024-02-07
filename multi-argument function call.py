#Question 1
#Write a Python program that asks the user to input two numbers and finds the max of those number when they are raised to the power of each other. 

#Display three numbers in your answer, the first number raised to the power of the second, the second number raised to the power of the first, and then the maximum of these two computed values, each on one line.


integer1 = input('Enter an integer>')
integer2 = input('Enter another integer>')
int1powint2 = int(integer1)**int(integer2)
int2powint1 = int(integer2)**int(integer1)
max1and2= max(int2powint1,int1powint2)
print(integer1 +' to the power of '+ integer2 +' is '+ str(int1powint2))
print(integer2 +' to the power of '+ integer1 +' is '+ str(int2powint1))
print('the max of '+str(int1powint2)+' and '+str(int2powint1)+' is '+ str(max1and2))


rhyme1 = 'Twinkle, twinkle'
rhyme2 = input('Finish the line >')
print(len(rhyme1), len(rhyme2))
print(len(rhyme1) + len(rhyme2))

from random import randint
rhyme = 'The wheels on the bus'
print(rhyme)
guess = int(input('how long is the rhyme >'))
length = len(rhyme)
answer = randint(guess, length)
print(answer)

rhyme1 = 'Star light, star bright'
rhyme2 = 'The first star I see tonight'
print(type(len), type(1.0))
print(len(rhyme1), len(rhyme2), dir(rhyme1, rhyme2))

a = 2
b = 2
a = pow(a,b)
b = pow(b,a)
c = a + b
print(a,b,c)
