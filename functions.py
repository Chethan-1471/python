def my_function():
  print("Hello from a function")
my_function()

#Hello from a function


def my_function(fname):
  print("Hello! "+ fname )

my_function("chethan")
#Hello! chethan

#Arbitary Arguments
def my_function(*letter):
  print("letter is " + letter[2])
my_function("A", "B", "C")
#letter is C