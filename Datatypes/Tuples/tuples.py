tuple = ("apple", "banana", "cherry")
print(tuple)

#('apple', 'banana', 'cherry')

tuple = ("apple", "banana", "cherry", "apple", "cherry")#allows duplicate values
print(tuple)

#('apple', 'banana', 'cherry', 'apple', 'cherry')


tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(tuple))

#5


thistuple = ("apple",)  #need to add a comma after the item to recognize it as a tuple
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#<class 'tuple'>
#<class 'str'>


thistuple = tuple(("apple", "banana", "cherry")) #double round-brackets
print(thistuple)


#('apple', 'banana', 'cherry')
