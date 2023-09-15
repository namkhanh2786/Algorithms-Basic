import random
randomList = []

for i in range(10):
    randomList.append(random.randint(1, 10))
randomList.sort() #sort the list
print(randomList)

a = int(input('Enter your number: '))
mid_index = int(len(randomList) / 2)
mid_value = randomList[mid_index]

found = 0 #False
#three conditions
if a == mid_value:
    print('Found: ', mid_index)
    found = 1
elif a < mid_value:
    for i in range(mid_index):
        if randomList[i] == a:
            found = 1
            print(randomList[i])
            break
else: #a > mid_value
    for i in range(mid_index, len(randomList) - 1):
        if randomList[i] == a:
            found = 1
            print(randomList[i])
            break

if found == 0:
    print("Cannot find your number")