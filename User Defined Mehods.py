def main():
    rect1 = Rectangle(5,10,15,20)
    rect2 = Rectangle(10,5,20,15)
    if rect1.intersects(rect2):
        print('Overlap')
    else:
        print('no overlap')


class Rectangle: 
    
    def __init__(self,corner_x,corner_y,width,height):
        self.x= corner_x
        self.y = corner_y
        self.width  = width
        self.height = height    
    def intersects(self,rect):
        return not ((self.x + self.width < rect.x) or (rect.x + rect.width < self.x) or (self.y + self.height < rect.y) or (rect.y + rect.height <self.y))

main()
 
 
from datetime import date

#Write a class definition for the Person class that includes the following user-defined methods:
class Person():
    def __init__(self,name,height,birthdate):
        self.name = name
        self.height = height
        self.birthdate = birthdate
    def get_name(self):
        return str(self.name)
    def get_height(self):
        return int(self.height)
    def get_age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age = today.year - self.birthdate.year-1
        return age         
    def get_description(self):
      # Return a string object of the form: Name is
      # N cm high and is M years old, where N and M
      # are integers
        age  = self.get_age()
        name = self.get_name()
        height = self.get_height()
        
        
        return (str(name) + ' is ' +str(height)+' cm high and is ' + str(age)+' years old.')
  
def main():
  # Create a person named 'Michael', with height
  # 190 cm, who was born on August 14, 1976 and
  # output a description of this individual.
    
    birthdate = date(1976, 8, 14) 
    name= 'Michael'
    height = 190
    person = Person(name, height, birthdate)
    print(Person.get_description(person))
    


main()
  

