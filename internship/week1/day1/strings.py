"""
Methods of string in python 
"""

# lower() method
name= "HUSSNAIN ZAFAR"
print(name.lower())

# upper() method
name= "hussnain zafar"
print(name.upper())

# strip() method
name= "   Hussnain Zafar   "
print(name.strip())

# replace() method
name = "Hussnain Ahmad"
print(name.replace("Ahmad", "Zafar"))

# split() method
name = "Hussnain,Zafar"
print(name.split(","))

# join() method
name = ["Hussnain ","Zafar"]
print("".join(name))

# find() method
name = "Hussnain Zafar"
print(name.find("Zafar"))

# startswith() method
name = "Hussnain Zafar"
print(name.startswith("hussnain"))
print(name.startswith("Hussnain"))

# endswith() method
name = "Hussnain Zafar"
print(name.endswith("Zafar"))
print(name.endswith("Hussnain"))

# count() method
name = "Hussnain Zafar"
print(name.count("H"))

# capitalize() method
name = "hussnain zafar"
print(name.capitalize())

# title() method
name = "hussnain zafar"
print(name.title())

# swapcase() method
name = "Hussnain zafar"
print(name.swapcase())

# format() method
name = "Hussnain"
age = 24
print("Hi my name is {} and i am {} years old".format(name,age))

# encode() method
name = "Hussnain Zafar"
print(name.encode())

# isalpha() method
name = "HUSSNAIN"
print(name.isalpha())

# isdigit() method
name = "1"
print(name.isdigit())

# isalnum() method
name = "Hussnain111"
print(name.isalnum())