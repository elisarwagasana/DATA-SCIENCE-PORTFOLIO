# Activity 13
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 10/07/2022

#!.
import random
def flipCoin():
    rand=random.randint(0,1)
    return rand
print(flipCoin())
print(flipCoin())
print(flipCoin())
print(flipCoin())
print(flipCoin())
print(flipCoin())
print(flipCoin())
print(flipCoin())
print(flipCoin())

#2.
def flipSeveralTimes(num):
    count=0
    for _ in range(num):
        rand=flipCoin()
        if rand==0:
            count=count+1
            print("H", end="")
        if rand==1:
            print("T", end="")
    print()
    return count
# flipSeveralTimes(10)
# flipSeveralTimes(10)
# flipSeveralTimes(10)
# flipSeveralTimes(10)
# flipSeveralTimes(10)

#3.
def flipUntilSame(num):
    count=0
    rand=1
    for y in range(num):
        while rand!=num and rand!=0:
            rand=flipSeveralTimes(num)
            count=count+1
    print(count)
    print("It took", count, "to get all heads or all tails with", num, "coins")
flipUntilSame(4)
        
    