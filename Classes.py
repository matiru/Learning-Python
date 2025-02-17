#CLASSES

#we can declare our own classes and in them we can instanciate objects

# object is an instance if a class

# class is the type of an object

class Animal :
    def walk(self):
        print("Night walker")
        
class Dog(Animal) : 
    
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
    
    def bark(self):
        print("wooof!")

nala = Dog("Nala",10)

print(nala.name)

print(nala.age)


nala.bark()
nala.walk()
