# reduce()

#used to calculate a value out of a sequence like a list

#long way
#expenses = [
    #('Dinner',80),
    #('Car repair' , 120)
    #]

#sum = 0 

#for expense in expenses :
    
    #sum += expense[1]

#print(sum)


from functools import reduce


expenses = [
    ('Dinner',80),
    ('Car repair' , 120)
    ]
sum = reduce (lambda a ,b : a[1] + b[1], expenses)

print (sum)