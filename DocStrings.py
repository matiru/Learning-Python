#Docstrings

def increment(n):
    """ Increment a number 
    
    sdsvdvs
    
    """
    return n  + 1
print (help(increment))



#Annotations


# specifying this takes an int an returns an int 
def increment(n: int) -> int:
  
    return n  + 1
