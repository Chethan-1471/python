#local scope
def func():
  c=500                       #local variable can be accessed from a function within the function
  def innerfunc():
    print(c)
  innerfunc()

func()

#500



#global scope

x = 300

def func():                #same variable same inside and outside of a function
  x = 200
  print(x)

func()

print(x)

#200
#300


"""To change the value of a global variable inside a function,  
by using global keyword"""
x = 100

def func():
  global x
  x = 300

func()

print(x)

#300
