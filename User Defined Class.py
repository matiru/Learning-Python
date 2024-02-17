def main():
    rect1 = create_rectangle(5,10,15,20)
    rect2 = create_rectangle(10,5,20,15)
    if rectangles_intersect(rect1,rect2):
        print('Overlap')
    else:
        print('no overlap')


def rectangles_intersect(r1,r2):
    return not ((r1.x + r1.width < r2.x) or (r2.x + r2.width < r1.x) or (r1.y + r1.height < r2.y) or (r2.y + r2.height <r1.y))



def create_rectangle(corner_x,corner_y,width,height):
    #component objects
    rect = Rectangle()# attribute reference
    rect.x= corner_x
    rect.y = corner_y
    rect.width  = width
    rect.height = height   
    print(type(rect))    
    return rect
class Rectangle: 
    pass


main()



#Write a class definition for the Person class and write user-defined functions with these function headers:
from datetime import date


def create_person(name, height, birthdate):
  # Return a a new person object with the given
  # name, height and birthdate.
  # - name is a str
  # - height is an int object in centimetres
  # - birthdate is a date object from the
  # module datetime
    person= Person()
    person.name= name
    person.height = height
    person.birthdate = birthdate
    return person

class Person():
    pass

def get_age(person):
    # Return the age of the person in years.
    today = date.today()
    age = today.year - person.birthdate.year
    if (today.month, today.day) < (person.birthdate.month, person.birthdate.day):
        age = today.year - person.birthdate.year-1

    return age 
def get_description(person):
      # Return a string object of the form: Name is
      # N cm high and is M years old, where N and M
      # are integers
    age  = get_age(person)
    return (str(person.name) + ' is ' +str(person.height)+' cm high and is ' + str(age)+' years old.')
  
def main():
  # Create a person named 'Michael', with height
  # 190 cm, who was born on August 14, 1976 and
  # output a description of this individual.
    
    birthdate = date(1976, 8, 14) 
    name= 'Michael'
    height = 190
    person = create_person(name, height, birthdate)
    print(get_description(person))
    


main()
  
