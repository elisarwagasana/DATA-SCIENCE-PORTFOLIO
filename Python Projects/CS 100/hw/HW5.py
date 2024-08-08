# HW5
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 10/31/2022

#TASK 0
# def getASCII(string):
#     string=input("Please enter a string:")
#     print("Please enter a string:")

    #for loop that prints out the ASCII value of each letter(character) in the string
#     for ch in string:
#         pos=ord(ch)
#         print(pos, end=" ")   
# getASCII("food")

#TASK 1 
# import random 
# def moreEvens():
#     count=0
#     countEven=0
#     countOdd=0
#     num=int(random.randint(0,99))

#     While loop that keeps the funtion running until more than 10 numbers have been produced and there are
#     more even numbers than odd numbers.
#     while count<=10 or countEven<countOdd:
#         print(num, end=" ")
#         count=count+1
#         If statements that counts the number of odd and even numbers produced.
#         if num%2==0:
#             countEven=countEven+1
#         else:
#             countOdd=countOdd+1
#         num=int(random.randint(0,99))
# moreEvens()

#TASK 2
# def Anagrams(string1, string2):
#     for loop that examines if a character/letter in string1 is also in string 2
#     for ch in string1:
#         result=string2.find(ch)
#         if result<0:
#             return False
#     return True
# string1="STOP"
# string2="POTS"
# print(Anagrams(string1,string2))
#     

#TASK 3

# import random
# def rollDice():
#     rand=int(random.randint(1,6))
#     return rand
# print(rollDice())
# 
# def rollNDice(numDice):
#     count=1
#     firstRoll=rollDice()
#     print(firstRoll, end="")

    # This is a for loop because we know
    # how many number of dice we want to roll
#     for x in range(numDice-1):
#         currentRoll=int(random.randint(1,6))
#         print(currentRoll, end="")
#         if firstRoll==currentRoll:
#             count=count+1
#     print()
#     if count==numDice:
#         return True
#     else:
#         return False
# print(rollNDice(3))
# 
# def flipUntilSame(numDice):
    #This helps the loop to get the loop started
#     count=1
#     result=rollNDice(numDice)

    # This is a while loop because we do not know
    # how many iterations it will take for all
    # the dice to have the same numbers or result
#     while result==False:
#         result=rollNDice(numDice)
#         count=count+1
#     print("Rolls", count, "until same")
#     return count
# # print("Rolls", count, "until same")        
# flipUntilSame(3)
    
#TASK 4

# def mouseMovement():
#     LEFT=0
#     RIGHT=1
#     distanceRight=15
#     distanceLeft=15
#     distanceTravelled=0
#     print("The mouse is", distanceRight, "feet from the LEFT end of the pipe")
#     print("The mouse is", distanceLeft,  "feet from the RIGHT end of the pipe")

#     While loop for the function to keep going until the distancetravelled is greater than 50 or the
#     distance travelled on either sides is greater than 30
#     while (0 <= distanceRight<=30 or 0 <= distanceLeft<=30) or distanceTravelled<=50:
#         rand=int(random.randint(0,1))
#         randDistance=int(random.randint(3,8))
#         distanceTravelled=distanceTravelled+randDistance
#         print()

#         Bolean expression to track the direction of the mouse
#         if rand==0:
#             print("The mouse moved", randDistance, "feet to the LEFT")
#         else:
#             print("The mouse moved", randDistance, "feet to the RIGHT")
#         
#         print("The mouse has travelled a total of", distanceTravelled)

#         Another Bolean expression to track how the mouse moves from both sides of the pipe
#         if rand==1:
#             distanceRight = distanceRight - randDistance
#             distanceLeft = distanceLeft+randDistance
#             print("The mouse is", distanceLeft, " from the LEFT of the pipe")
#             print("The mouse is", distanceRight, " from the RIGHT of the pipe")
#             print()
#         else:
#             distanceLeft=distanceLeft-randDistance
#             distanceRight = distanceRight + randDistance
#             print("The mouse is", distanceLeft, " from the LEFT of the pipe")
#             print("The mouse is", distanceRight, " from the RIGHT of the pipe")
#             print()

#         This Bolean expression is to help us to know if the mouse escaped from either sides or did not escape      
#         if distanceLeft>=30:
#             print("The mouse escape from the RIGHT end of the pipe!")
#             return 0
#             print()
#         elif distanceRight>=30:
#             print("The mouse escape from the LEFT end of the pipe!")
#             return 0
#             print()
#
#         if distanceTravelled>=50:
#             print("The mouse went more than 50 feet and did not escape!")
#             return 0
#             print() 
#     
# mouseMovement()

chr(5 + ord('a'))