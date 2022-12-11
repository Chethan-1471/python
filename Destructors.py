class student:

	# Initializing
	def __init__(self):
		print('student created.')

	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, student deleted.')

obj = student()
del obj

#student created.
#Destructor called, student deleted.