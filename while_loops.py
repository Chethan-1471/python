i = 1
while i < 6:
  print(i,end=" ")
  i += 1
#1 2 3 4 5

#to print $ 1 2 3 + 4 5 6 + 7 8 9 $

print("$",end=" ")
i = 1
while i < 6:
  print(i,end=" ")
  if i == 3:
    break
  i += 1
print("+",end=" ")
i = 4
while i < 7:
  print(i,end=" ")
  if i ==7:
    break
  i += 1
print("+",end=" ")
while i < 10:
  print(i,end=" ")
  if i ==10:
    break
  i += 1
print("$",end=" ")


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

"""1
2
3
4
5
i is no longer less than 6"""


