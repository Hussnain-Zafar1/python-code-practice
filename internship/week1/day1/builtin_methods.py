
# len() method

print(len("Hello"))
print(len([1, 2, 3]))
print(len({"a": 1, "b": 2}))
print(len({1, 2, 3, 4}))

# range() method
print(list(range(5)))
print(list(range(2, 10)))
print(list(range(1, 10, 2)))

#range method is commonly used in for loops to iterate over a sequence of numbers
for i in range(5):
    print(i)

# enumerate() method      its actually used when we need index with the value of the list or any iterable
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index,"->",fruit)



# sorted() method
nums = [1,4,3,5,2,1]
sorted_num = sorted(nums,reverse=True)
print(sorted_num)
print(sorted("Hussnain")) 


# sum() method
nums=[1,4,3,5,2]
print(sum(nums))

# max() method
nums=[1,4,3,5,2]
print(max(nums))

# min() method
nums=[1,4,3,5,2]
print(min(nums))

# isinstance() method
print(isinstance(5, int))
print(isinstance(5, float))
print(isinstance(5, str))
print(isinstance(5.0, float))
print(isinstance("Hello", str))
print(isinstance([1, 2, 3], list))
print(isinstance({"a": 1, "b": 2}, dict))
print(isinstance({1, 2, 3}, set))