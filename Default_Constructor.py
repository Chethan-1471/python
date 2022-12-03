#syntax of constructor
"""def __init__(self):
    # body of the constructor"""

#default constructor-has only one argument
# which is a reference to the instance being constructed

class person:

	# default constructor
	def __init__(self):
		self.name = "batman"

	# a method for printing data members
	def print_character(self):
		print(self.name)
# creating object of the class
obj = person()
# calling the instance method using the object obj
obj.print_character()

#batman


