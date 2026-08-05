
person = {"name": "Hussnain", "age": 24}

# get() method
print(person.get("age"))

# items() method
print(person.items())

# the items() method is actually useful when we have to loop through both key and value
for key , value in person.items():
    print(key,"->",value )

# keys() method
print(person.keys())

# values() method
print(person.values())

#update() method
person.update({"age": 25,"city":"lahore"})
person.update({"country":"Pakistan"})
print(person)

# pop() method
person.pop("name")
print(person)

# setdefault() method
person.setdefault("gender","male")
person.setdefault("age",30)
print(person)
