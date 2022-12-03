#parameterized constructor-it takes first argument as a reference
#to the instance being constructed called-self and other reset argument provided by programmer


class Addition:
	first = 0
	second = 0
	answer = 0

	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()


"""First number = 1000
Second number = 2000
Addition of two numbers = 3000
First number = 10
Second number = 20
Addition of two numbers = 30
"""

