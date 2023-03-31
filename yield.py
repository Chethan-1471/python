# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time


def simpleGeneratorFun():
	yield 11
	yield 12
	yield 13


# Driver code
for i in simpleGeneratorFun():
	print(i)

#11
#12
#13



# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1


def nextSquare():
	i = 1

	# An Infinite loop to generate squares
	while True:
		yield i*i
		i += 1 # Next execution resumes
		# from this point


# Driver code to test above generator
# function
for num in nextSquare():
	if num > 100:
		break
	print(num)
"""
1
4
9
16
25
36
49
64
81
100
"""

# Python3 code to demonstrate yield keyword

# Use of yield
def printresult(String) :
	for i in String:
		if i == "e":
			yield i

# initializing string
String = "GeeksforGeeks"
ans = 0
print ("The number of 'e' in word is : ", end = "" )
String = String.strip()

for j in printresult(String):
	ans = ans + 1

print (ans)

#The number of 'e' in word is : 4



