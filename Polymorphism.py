#polymorphism
#genearalises a  function so it can wor on different types
#class Dog:
    #def eat(self):
        #print('Eating dog food')

#class Cat:
    #def eat(self):
        #print('Eating cat food')
        
#animal1 = Dog()
#animal2 = Cat()

#animal1.eat()
#animal2.eat()


##Operator Overloading

#a technique used to make classes comparable and to make them work with python operators


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __gt__(self,other):
        return True if self.age > other.age else False
        
roger = Dog('Roger',8)
syd= Dog ('Syd', 7)


print(roger > syd)