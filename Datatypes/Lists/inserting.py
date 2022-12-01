list = ["apple", "banana", "cherry"]
list.insert(1, "orange")
print(list)

#-['apple', 'orange', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#-['apple', 'banana', 'cherry', 'orange']


list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
list.extend(tropical)
print(list)

#-['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']



list = ["apple", "banana", "cherry"]
tuple = ("kiwi", "orange")
list.extend(tuple)
print(list)

#-['apple', 'banana', 'cherry', 'kiwi', 'orange']
