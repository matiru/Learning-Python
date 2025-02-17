

#def hello(name="my friend"):
    #print ('Hello' + name)
    

#hello()
#hello("gEM")


#def change(value) :
    #value["name"] = "mat"
    #print(value)
    
    

#val = {"name":"gem"}

#change(val)

#print (val)


#def hello(name):
    #print("hello " + name)
    #return name , "Beau", 8

#print(hello("gem"))



######
##closures

def counter():
    
    count = 0 
    
    def increment():
        
        nonlocal count
        
        count =  count + 1
        
        return count
    
    #print(increment())
    return increment

increment = counter()

print(increment())

print(increment())