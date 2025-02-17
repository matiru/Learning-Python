#filter()

# takes an iterable and returns a filter object which is another iterable but with less items


numbers = [1,2,3,4,5,6,7,8,]

def isEven(n):
    return n % 2 == 0


result = filter (isEven ,numbers)

result = filter (lambda n:n %2 == 0 ,numbers)

print(list(result))


