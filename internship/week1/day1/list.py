"""
practicing lists as a stack and queue
"""

from collections import deque

#append() method
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.append(["berry"])
print(fruits)

# extend() method
fruits = ["apple", "banana", "cherry"]
fruits.extend(["mango","berry"])
print(fruits)

# pop() method
fruits = ["apple", "banana", "cherry"]
fruits.pop()
fruits.pop(1)  #pop method also takes index
print(fruits)

# sort() method
fruits = ["banana", "apple", "cherry"]
fruits.sort(reverse=True)
print(fruits)

# sort() method
fruits = [2,4,1,6,9]
fruits.sort()
print(fruits)


# copy() method
fruits = ["apple", "banana", "berry",["mango","kiwi"]]
fruits_copy = fruits.copy()
# print(fruits_copy)
fruits_copy[3].append("orange")
print(fruits)


# queue implementation
fruits = deque(["apple", "banana", "berry"])
fruits.append("kiwi")
print(fruits)
fruits.append("orange")
print(fruits)
fruits.popleft()
print(fruits)
fruits.popleft()
print(fruits)