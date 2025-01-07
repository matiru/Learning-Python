 #Write a python function that receives five numbers as input and finds the largest of five numbers.
#Print the results to the console. 
def  findlargestnumber (a,b,c,d,e):
 arguments = [a,b,c,d,e]
 index = 0
 largest = arguments[index]
 for arg in arguments:
  if arguments[index] > largest :
   largest = arguments[index]
  index += 1
 return print(largest)
  
 
findlargestnumber(21,11,333,22,55)
   
   
    
