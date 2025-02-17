# map(),filter() ,reduce()


#1map()

# is used to run a function upon each item in an iteral item  eg list and
# create a new list with same number of items but the values of each item can be changed

numbers =[1,2,3,]

def double(a):
    return a * 2


result  = map(double, numbers)

print (list(result))
