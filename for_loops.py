fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

"""apple
banana
cherry"""


for x in range(6):
  print(x)
else:
  print("Finally finished!")

"""0
1
2
3
4
5
Finally finished!"""


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
"""red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry"""

