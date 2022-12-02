class Person:                               #Person class to create an object
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):                #using  the printname method
    print(self.firstname, self.lastname)



c= Person("walt", "junior")
c.printname()
#walt junior



#creating a child class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):   #creating child class called student
  pass

c= Student("doc", "walter")
c.printname()


#doc walter