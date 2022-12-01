thisset = ("apple", "banana", "cherry") 
print(thisset)

#-('apple', 'banana', 'cherry')



set = {"apple", "banana", "cherry"}

for x in set:
  print(x)
"""banana
cherry
apple
"""

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#{'cherry', 'apple'}


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

""'cherry
apple
banana
"""



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#{'apple'}