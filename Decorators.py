#decorators

#are a way to change ,enhance or alter in any way how a function works 

#a decorator is a function that takes a function as a parameter wraps the function in an inner function,
# that performs the job it has to do and returns that inner function


def logtime(func):
    def wrapper():
        print("before")
        val= func()
        print("after")
        return val
    
    return wrapper  


@logtime
def hello():
    print("Hello!")


hello()