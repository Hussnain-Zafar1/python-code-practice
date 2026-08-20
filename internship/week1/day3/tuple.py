# we only have two methods for tuple because its immutable and does not allow to insert, update and delete elelments after the creation
numbers = (1,2,3,2,4,5,6,5)

# count() method
print(numbers.count(2))

# index method
print(numbers.index(2,2,5))

# we also have some tuple operations

#concatination
t1 = (1,2)
t2 = (3,4)
t3 = t1 + t2
print(t3)

# repetition
print(numbers * 2)

# membership
print(1 in numbers)
print(10 in numbers)


#maximun
print(max(numbers))

#minimum
print(min(numbers))

# sorted()
print(sorted(numbers))     #by default it returns a list
print(tuple(sorted(numbers)))   # convert the sorted list to tuple
