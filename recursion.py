number = int(input('Enter a number to recursive plus from 1 to n: '))

def toN(number):
    if (number == 0): #base condition
        return 0
    return number + toN(number-1) #recursion part - 5 + 4 + 3 + 2 + 1

print(toN(number))