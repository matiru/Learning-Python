import time
sleep = input('Enter sleep mode>')
print(sleep)
time.sleep(1)
if sleep == 'REM':
    print('Dreams likely')
else :
    print('Dreams unlikely')
    


from time import sleep as pause
sleep = input('Enter sleep mode>')
print(sleep)
pause (1)
if sleep == 'REM':
    print('Dreams likely')
else :
    print('Dreams unlikely')
    
    

from math import sqrt as root

def sqrt(value):
      # Return a number that is the argument value
      # raised to the argument value power
    
    return_value = int(value**value)
    
    return return_value
      
      
      
def main():
    my_int=input('Enter a positive integer >')
    my_int2 = root(int(my_int))
    return_value=sqrt(int(my_int2))
    root_value = root(return_value)
    print('The magic value for '+ my_int + ' is ' +str(root_value))
    
  # Input a positive integer, call the sqrt
  # function from the math module using the
  # input value as an argument. Then, call the
  # above sqrt function on the result and call
  # the sqrt function from the math module on
  # that result. Finally, print the input number
  # and the final result.
main()