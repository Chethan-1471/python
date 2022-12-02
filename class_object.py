#class


class person:

	# A simple class
	# attribute
	attr1 = "elon musk"
	attr2 = "spacex"

	# A sample method
	def fun(self):
		print("I'm ", self.attr1)
		print("I'm ceo of", self.attr2)


# Driver code
# Object instantiation
object = person()

# Accessing class attributes
# and method through objects
print(object.attr1)
object.fun()



"""elon musk
I'm  elon musk
I'm ceo of spacex"""