a ={1,2,3,4,5}
b ={4,5,6,7,8}

# add() method
a.add(9)
print(a)

# update() method
a.update(b)
print(a)

# union() method
c=a.union(b)
print(c)

# intersection() method
c = a.intersection(b)
print(c)

# difference() method
print(a.difference(b))

# discard() method
a.discard(4)
print(a)
