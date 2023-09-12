import random
listnumber = [] #empty list

for i in range(10):
  listnumber.append(random.randint(1, 10))
print(listnumber)

findNum = int(input('Enter your number: '))
found = 0 #0 is false
for i in range(10):
  if listnumber[i] == findNum:
    found = 1
    print('Found: ', findNum, ' at ', i)
    break
if found == 0:
  print('Cannot find your number')