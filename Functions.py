def banner():
    for letter in word:
        print(' ' * indent + letter)

word = 'blue'
indent =  3
banner()
print(word)
print(type(banner))
        

def add():
  sum = operand1 + operand2
  print(sum)
  operand1 = 0
operand1 = int(input('Enter an integer >'))
operand2 = int(input('Enter an integer >'))
add()
print('is', operand1, 'plus', operand2)


def add():
  sum = operand1 + operand2
  print(sum)
operand1 = int(input('Enter an integer >'))
operand2 = int(input('Enter an integer >'))
add()
print('is', operand1, 'plus', operand2)


def add():
  operand1 = 0
  sum = operand1 + operand2
  print(sum)
operand1 = int(input('Enter an integer >'))
operand2 = int(input('Enter an integer >'))
add()
print('is', operand1, 'plus', operand2)


def add():
  operand2 = 10
  sum = operand1 + operand2
  print(sum)
operand1 = int(input('Enter an integer >'))
add()
print('is', operand1, 'plus', operand2)



#def stats():
  ## Output the list that the global identifier
  ## my_list is bound to and the mean and
  ## the population standard deviation of the
  ## numbers in the list, rounded to two decimal
  ## places
  ##[2, 4, 6, 8, 10, 12]
  ##mean is 7.0
  ##population standard deviation is 3.42  
  
import math  

my_list = [47, 34, 72, 56, 13, 98, 46, 4]
def stats():
    sum = 0
    dev = 0
    sum2 = 0
    dev_list= []
    dev_list2 =[]
      
    for number in range(0,len(my_list)):   
        sum = my_list[number] + sum 
      
    mean =  sum / len(my_list)
  
    for number in range(0,len(my_list)):       
        dev_value = ((int(my_list[number])- (mean)) **2)
        dev_list.append(dev_value)
        sum2 = dev_list[number] + sum2
        dev = math.sqrt(sum2 /len(my_list))
      
    print(my_list)
    print('mean is '+ str(round(mean,2)) )
    print('population standard deviation is ' + str(round(dev,2)))


stats()
  

def banner (word,indent):
    for letter in word:
        print(' '*indent + letter)

word1 = 'blue'
word2 = 'red'
indent1 = 3
indent2 = 5
banner(word1,indent1)
banner(word2, indent2)
print(word1,word2)



def diff(parm1, parm2):
  diff1 = parm1 - parm2
  arg1 = 20
  diff2 = arg1 - arg2
  print(diff1, diff2)
arg1 = int(input('Enter an integer >'))
arg2 = int(input('Enter an integer >'))
diff(arg1, arg2)
print(arg1, arg2)


def diff(parm1, parm2):
  diff1 = parm1 - parm2
  parm1 = 20
  diff2 = arg1 - arg2
  print(diff1, diff2)
arg1 = int(input('Enter an integer >'))
arg2 = int(input('Enter an integer >'))
diff(arg1, arg2)
print(arg1, arg2)


def diff(parm1, parm2):
  diff1 = parm1 - parm2
  parm1 = 20
  diff2 = arg1 - arg2
  print(diff1, diff2)
arg1 = int(input('Enter an integer >'))
arg2 = int(input('Enter an integer >'))
diff(arg1, arg2)
print(parm1, parm2)



def diff(parm1, parm2):
  diff1 = parm1 - parm2
  parm1 = 20
  diff2 = parm2 - parm1
  print(diff1, diff2)
parm1 = int(input('Enter an integer >'))
parm2 = int(input('Enter an integer >'))
diff(parm2, parm1)
print(parm1, parm2)


def diff(parm1, parm2):
  diff1 = parm1 - parm2
  arg2 = 20
  diff2 = arg1 - arg2
  print(diff1, diff2)
arg1 = int(input('Enter an integer >'))
arg2 = int(input('Enter an integer >'))
diff(arg1)
print(arg1, arg2)


#def largest_two(target_list):
  ## Output the argument list, the largest
  ## element in the list and the second largest
  ## element in the list
  


my_list=[4, 2, 8, 7, 8]

def largest_two(target_list):
    copy_list = target_list.copy()
    largest = max( copy_list )
    copy_list.remove(largest) 
    second_largest = max(copy_list)
    print('The largest and second largest elements in the list ' + str(my_list)+ 'are '+ str(largest)+' and '+str(second_largest))
largest_two(my_list)


def magic(abra, cadabra):
  abra = abra + cadabra
  print(abra)
  confusion(abra, cadabra)
def confusion(cadabra, word1):
  confused = cadabra + word1
  print(confused)
def main():
  word1 = input('Enter a word >')
  word2 = input('Enter a word >')
  magic(word1, word2)
  print(word1, word2)
main()

def magic(abra, cadabra):
  abra = abra + cadabra
  print(abra)
  confusion(abra, cadabra)
def confusion(cadabra, word1):
  confused = cadabra + word1
  print(confused)
def main():
  word1 = input('Enter a word >')
  word2 = input('Enter a word >')
  magic(word1, word2)
  confusion(word2, word2)
main()

def magic(abra, cadabra):
  abra = abra + cadabra
  print(abra)
  confusion(abra, cadabra)
def confusion(cadabra, word1):
  confused = cadabra + word1
  print(confused)
def main():
  word1 = input('Enter a word >')
  word2 = input('Enter a word >')
  magic(word1, word2)
  print(confused)
main()


def magic(abra, abra):
  abra = abra + cadabra
  print(abra)
  confusion(abra, cadabra)
def confusion(cadabra, word1):
  confused = cadabra + word1
  print(confused)
def main():
  word1 = input('Enter a word >')
  word2 = input('Enter a word >')
  magic(word1, word2)
  print(word1, word2)
main()


def magic(abra, cadabra):
  abra = abra + cadabra
  print(abra)
  confusion(abra, cadabra)
def confusion(cadabra, word1):
  confused = abra + cadabra
  print(confused)
def main():
  word1 = input('Enter a word >')
  word2 = input('Enter a word >')
  magic(word1, word2)
  print(word1, word2)
main()


def magic(abra, cadabra):
  abra = abra + cadabra
  print(abra)
  confusion(abra, cadabra)
def confusion(cadabra, word1):
  confused = abra + cadabra
  print(confused)
def main():
  word1 = input('Enter a word >')
  word2 = input('Enter a word >')
  magic(word1, word2)
  print(word1, word2)
main()










#def string_lengths(string_list):
    ## Create a new list that contains the
    ## lengths of the strings in the argument
    ## list or an empty list if the argument list
    ## is empty. Output the original list and the
    ## length list.


    
    
    
def string_lengths(string_list):
    copy_list = string_list.copy()
    length_list = []
    for word in copy_list:
        wordlen=len(word)
        length_list.append(wordlen)
    print(length_list)

def main():
    my_string = input('Enter some words >')
    string_list=(my_string.split())
    print(string_list)   
    string_lengths(string_list)
main()