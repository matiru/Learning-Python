def mix(index1, index2):
  colors = ('white', 'red', 'purple', 'orange', 'blue', 'white', 'green', 'white', 'white', 'yellow')
  if index1 == 0:
      mix_index = index2*index2
  elif index2 == 0:
      mix_index = index1*index1
  else:
      mix_index = index1*index2
  mix_color = colors[mix_index]
  return mix_color
def main():
  colors = ('white', 'red', 'blue', 'yellow')
  for color in colors:
    tint = input('Enter one of: ' + str(colors))
    color_index = colors.index(color)
    tint_index = colors.index(tint)        
    result_color = mix(color_index, tint_index)
    print(color, '+', tint, '=', result_color)
main()







def mix(index1, index2):
  colors = ('white', 'red', 'purple', 'orange', 'blue', 'white', 'green', 'white', 'white', 'yellow')
  if index1 == 0:
      mix_index = index2*index2
  elif index2 == 0:
      mix_index = index1*index1
  else:
      mix_index = index1*index2
  mix_color = colors[mix_index]
  return mix_index
def main():
  colors = ('white', 'red', 'blue', 'yellow')
  for color in colors:
    tint = input('Enter one of: ' + str(colors))
    color_index = colors.index(color)
    tint_index = colors.index(tint)        
    result_color = mix(color_index, tint_index)
    print(color, '+', tint, '=', result_color)
main()



def mix(index1, index2):
  colors = ('white', 'red', 'purple', 'orange', 'blue', 'white', 'green', 'white', 'white', 'yellow')
  if index1 == 0:
      mix_index = index2*index2
  elif index2 == 0:
      mix_index = index1*index1
  else:
      mix_index = index1*index2
  mix_color = colors[mix_index]

def main():
  colors = ('white', 'red', 'blue', 'yellow')
  for color in colors:
    tint = input('Enter one of: ' + str(colors))
    color_index = colors.index(color)
    tint_index = colors.index(tint)        
    result_color = mix(color_index, tint_index)
    print(color, '+', tint, '=', result_color)
main()



def mix(index1, index2):
  colors = ('white', 'red', 'purple', 'orange', 'blue', 'white', 'green', 'white', 'white', 'yellow')
  if index1 == 0:
      mix_index = index2*index2
  elif index2 == 0:
      mix_index = index1*index1
  else:
      mix_index = index1*index2
  mix_color = colors[mix_index]
return mix_color
def main():
  colors = ('white', 'red', 'blue', 'yellow')
  for color in colors:
    tint = input('Enter one of: ' + str(colors))
    color_index = colors.index(color)
    tint_index = colors.index(tint)        
    result_color = mix(color_index, tint_index)
    print(color, '+', tint, '=', result_color)
main()


def mix(index1, index2):
  colors = ('white', 'red', 'purple', 'orange', 'blue', 'white', 'green', 'white', 'white', 'yellow')
  if index1 == 0:
      return 'white'
  elif index2 == 0:
      mix_index = index1*index1
  else:
      mix_index = index1*index2
  mix_color = colors[mix_index]
  return mix_color
def main():
  colors = ('white', 'red', 'blue', 'yellow')
  for color in colors:
    tint = input('Enter one of: ' + str(colors))
    color_index = colors.index(color)
    tint_index = colors.index(tint)        
    result_color = mix(color_index, tint_index)
    print(color, '+', tint, '=', result_color)
main()




colors = ('white', 'red', 'purple', 'orange', 'blue', 'white', 'green', 'white', 'white', 'yellow')
def mix(index1, index2):
  if index1 == 0:
      mix_index = index2*index2
  elif index2 == 0:
      mix_index = index1*index1
  else:
      mix_index = index1*index2
  mix_color = colors[mix_index]
  return mix_color
colors = ('white', 'red', 'blue', 'yellow')
def main():
  for color in colors:
    tint = input('Enter one of: ' + str(colors))
    color_index = colors.index(color)
    tint_index = colors.index(tint)        
    result_color = mix(color_index, tint_index)
    print(color, '+', tint, '=', result_color)
main()




#def as_integer(an_object):
  ## If the argument is a string that represents
  ## a valid integer return that integer.
  ## Otherwise, return the NoneType object.


#def main():
  ## Call the as_integer function for each
  ## element in the list: ['20', 10, len, True, '-six', '-10', '0']
  ## and output the result object on its own line
  



def as_integer(an_object):
  
  if type(an_object) != str:
      result = None
  else:
  
    if an_object.replace('-','').isdigit():
      result = int(an_object)
    else:
      result = None
  return result
  
def main():
  
  list=['20', 10, len, True, '-six', '-10', '0']
  
  for item in list:
    result = as_integer(item)
    print(result)


#def filter_ints(word_list):
  ## Return a tuple containing two lists.
  ## The first list should contain an int
  ## for each element of the argument list
  ## that is a string that represents
  ## a valid integer. The second list should
  ## contain all the elements of the argument
  ## list that do not represent valid integers.
  
##def main():
  ### Prompt the user to enter some integers,
  ### separated by blanks. Output a list of the
  ### valid integers and the sum of these
  ### integers. If the list contains some
  ### "words" that are not valid integers, then
  ### output a list of these "error words". If not,
  ### do not output a list of these "error words".  
  
def as_integer(an_object):
  
  if type(an_object) != str:
      result = None
  else:
  
    if an_object.replace('-','').isdigit():
      result = int(an_object)
    else:
      result = None
  return result
  
def main():
  
  list=['20', 10, len, True, '-six', '-10', '0']
  
  for item in list:
    result = as_integer(item)
    print(result) 
    
word_list = ['hello', '5', len, 10, True] 
def filter_ints(word_list):
 
  str_valid_int =[]
  invalid_int=[]
  

  for item in word_list:  
    if type(item) != str:
      invalid_int.append(item)
    else:
      if item.replace('-','').isdigit():
          str_valid_int.append(item)
      if not item.replace('-','').isdigit():
          invalid_int.append(item)      
    
  #print(invalid_int)
  #print(str_valid_int)
#filter_ints(word_list)
    result_tuple=(str_valid_int,invalid_int)
    
    return result_tuple    
  
def main ():
  
  my_string = input('Enter some integers >')
  word_list=(my_string.split())  
  filter_ints(word_list)
  integer_list=[]
  error_list = []
  sum = 0
  for item in word_list:
    if item.replace('-','').isdigit():
      integer_list.append(int(item))
    else:
      error_list.append(item)
  for index in range(0, len(integer_list)):
    sum = sum + (integer_list[index] )  
  print('The sum of: '+ str(integer_list) +' is '+ str(sum))
  if len(error_list):
    print('These words are not integers: '+ str(error_list))
    
main()


