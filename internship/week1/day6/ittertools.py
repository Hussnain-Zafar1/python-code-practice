# from ittertools import count

# id_generator = count(5)
# print(next(id_generator))

from itertools import cycle , count,repeat , chain,islice,filterfalse,pairwise,starmap,tee


id_generator = count(5)
print(next(id_generator))
print(next(id_generator))
print(next(id_generator))

colors = cycle(["red", "green", "blue"])

print(next(colors)) 
print(next(colors))
print(next(colors))
print(next(colors)) 
print(next(colors))


servers = cycle(["server1", "server2", "server3"])
for i in range(6):
    server = next(servers)
    print(f"server: {server}")
# we can use above stratergy for the round robin

numbers = repeat("hello")
print(next(numbers))
print(next(numbers))
print(next(numbers))

a = [1,2,3]
b = ["a","b","c"]
combined = chain(a,b)
print(list(combined))


numbers = range(20)
print(list(islice(numbers, 0, 10, 2)))


numbers = [1, 2, 3, 4, 5, 6]
result = filterfalse(lambda x: x % 2 == 0, numbers)
print(list(result))

numbers = [1,2,3,4,5,6]
print(list(pairwise(numbers)))


result = starmap(pow, [
    (2, 3),
    (4, 2),
    (3, 3)
])
print(list(result))


numbers = iter([1, 2, 3, 4, 5,6,7,9])
a,b = tee(numbers, 2)
print(list(a))
print(list(b))
