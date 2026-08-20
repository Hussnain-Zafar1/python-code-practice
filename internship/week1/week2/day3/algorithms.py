# linear search

def linear_search(numbers,target):
    for i, number in enumerate(numbers):
        if number == target:
            return i
        

print(linear_search([1,2,34,5,6,7],7))


# binary search 


def binary_search(number,target):
    left,right = 0, len(number)-1
    while left<= right:
        middle = (left+right)//2
        if number[middle]== target:
            return middle
        elif number[middle]>target:
            right = middle -1
        else:
            left = middle + 1

print(binary_search([1,2,3,4,5,6,7],5))


