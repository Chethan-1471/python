a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#a is greater than b


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#=


#AND

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Both conditions are True


#OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#At least one of the conditions is True

#Nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#Above ten,
#and also above 20!





