word = input('Enter a word :')
while word != '':
    if len(word) < 6 :
        print('I do not like the word ' + word)
    else:
        print('I like the word ' + word)
    word = input('Enter a word:')


#number_string = input('Enter a postive integer >')
#sum = 0
#while number_string != 'stop':
  #number = int(number_string)
  #sum = sum + number
  #number_string = input('Enter a postive integer >')
#print(sum)


#number_string = input('Enter a postive integer >')
#sum = 0
#while number_string != 'stop':
  #number_string = input('Enter a postive integer >')
  #number = int(number_string)
  #sum = sum + number
#print(sum)


#number_string = '0'
#sum = 0
#while number_string != 'stop':
  #number = int(number_string)
  #sum = sum + number
  #number_string = input('Enter a postive integer >')
#print(sum)



















##Question 1
##Prompt the user to enter the Fibonacci numbers in order until the user either makes a mistake or enters the first Fibonacci number greater than 50. If the user makes an error, output a consolation message as shown in the sample run and end the program. If the user enters all of the Fibonacci numbers successfully then output a congratulations message as shown in the sample runs and end the program. Some people start the Fibonacci numbers and 0 and some people start at 1. In this question, we will start at 1


## The Fibonacci sequence is a type series where each number is the sum of the two that precede it. 

fib_list = [0]
index = 0
next_num = 0
first = input("Enter the next Fibonacci number >")

if not first.isdigit():
    print('Try again')
else:
    first = int(first)
    if first != 1:
        print('Try again')
    else:
        fib_list.append(first)
        while next_num <= 55:
            another = input("Enter the next Fibonacci number >")
            
            if not another.isdigit():
                print('Try again')            
            another = int(another)
            if (another) != (fib_list[index] + fib_list[(len(fib_list)-1)]):
                print('Try again')
                break
            else:
                fib_list.append(another)
                index = index + 1
                next_num = fib_list[index] + fib_list[(len(fib_list)-1)]
                
        okay = next_num
        print(okay)
        if okay-34 == 55:
            print("well done")                


            

 
            my_tuple = (2, 4, 6, 8)
            my_list = [10, 20, 30]
            length = len(my_tuple)
            for index in range(0, length):
              my_list[index] = my_list[index] + my_tuple[index]
            print(my_list)



            #1.
            #Question 1
            #Write a program that inputs words from the user, one per line and saves the words in a list until the user enters the word stop. The word stop should not be included in the list. The program should then output the list. It should then replace each word in the word list, whose index is even by its  index  multiplied by the length of the word. It should then output this modified list.
            

my_list =[]
word = input('Enter a word >')
while word !='stop':
    my_list.append(word)
    word=input('Enter a word >')
print(my_list)

for index in range(0,len(my_list)):
    if index % 2 == 0:
        my_list[index]= index * len(my_list[index])
print(my_list)