def reverse(word):
    my_list = list(word)
    my_list.reverse()
    reverse_string = ''.join(my_list)
    return reverse_string
def elaborate(word_list, word):
    reversed = reverse(word)
    word_list.insert(0, word)
    word_list.append(reversed)  
def main():
    words = []
    word = input('Enter a word >')
    while word != 'stop':
        elaborate(words, word)
        word = input('Enter a word >')
    print(words)
main()


def reverse(word):
    my_list = list(word)
    my_list.reverse()
    reverse_string = ''.join(my_list)
    return reverse_string
def elaborate(word_list, word):
    reversed = reverse(word)
    print(word_list)
    word_list = word_list.insert(0, word)
    print(word_list)
    #word_list.append(reversed)  
def main():
    words = []
    word = input('Enter a word >')
    while word != 'stop':
        elaborate(words, word)
        word = input('Enter a word >')
    print(words)
main()

def main():
    words =()
    word =  input('Enter a word >')
    while word != 'stop':
        words.insert(0, word)  
        word =input('Enter a word >')
    print(words)
main()
        
def reverse(word):
    reverse_string = word.reverse()
    return reverse_string
    
def elaborate(word_list, word):
    #reversed = reverse(word)
    word_list.insert(0, word)
    print(word_list)
    #word_list.append(reversed)
    
def main():
    words = []
    word = input('Enter a word >')
    while word != 'stop':
        elaborate(words, word)
        word = input('Enter a word >')
    print(words)
main()    


###def reverse(word):
    ###my_list = list(word)
    ###my_list.reverse()
    ###reverse_string = ''.join(my_list)
    ###return reverse_string
###def elaborate(word_list, word):
    ###reversed = reverse(word)
    ###word_list = word_list.insert(0, word)
    ###word_list.append(reversed)  
###def main():
    ###words = []
    ###word = input('Enter a word >')
    ###while word != 'stop':
        ###elaborate(words, word)
        ###word = input('Enter a word >')
    ###print(words)
###main()
    
    
    



def append_fibonacci(integer_list):
  ## Modify the argument list of integers by
  ## appending a new integer that is the sum
  ## of the last two integers in the list.
  ## If the list has fewer than two elements
  ## add the int object 1 to the list.
        if len(integer_list) < 2:
            integer_list.append(1)
        else:
            integer_list.append(integer_list[len(integer_list)-1]+integer_list[len(integer_list)-2])
        #return integer_list
    

def main():
  ## Call the append_fibonacci function on this
  ## list: [3, 5, 8] and output the result object
    integer_list = [3]
    append_fibonacci(integer_list)
    print(integer_list)
    #print( append_fibonacci(integer_list))
main()
  
  
def append_fibonacci(integer_list):
    # Modify the argument list of integers by
    # appending a new integer that is the sum
    # of the last two integers in the list.
    # If the list has fewer than two elements
    # add the int object 1 to the list.  
    if len(integer_list) < 2:
        integer_list.insert(0,1)
   
  
def fibonacci(max_int):
    # Return a list that contains all Fibonacci
    # numbers that are less than or equal
    # to the argument integer.
    if max_int == 0:
        integer_list = []
    else:
        integer_list = []
        integer_list.append(max_int)
        
        append_fibonacci(integer_list)
        integer_list.remove(max_int)
       
        index = 0
        count = 1
        next_num  = 1
        
        while next_num <= max_int:
            integer_list.append(next_num)
            next_num = integer_list[len(integer_list)-1]+integer_list[len(integer_list)-2]
            
    return(integer_list)   
       
        
    
  
def main():
    # Input a non-negative integer, n. Output
    # the Fibonacci numbers that are less than
    # or equal to that number, in order. If the
    # input is not a valid non-negative integer,
    # output a warning message.  
    
    non_negative_int= input('Enter a non_negative integer >')
    
    if not non_negative_int.isdigit():
        print(str(non_negative_int) + ' is not a non-negative integer')
    else:
        max_int = int(non_negative_int)
        print('The Fibonacci series starts with: ' +str(fibonacci(max_int)))
        
main()