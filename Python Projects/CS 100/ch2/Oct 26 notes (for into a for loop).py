import random
numbers=int(input("please enter how many lines:"))

for count in range(numbers):
    num=random.randint(0,10)
    for count in range(num):
        print(num, end=" ")
    print()
    