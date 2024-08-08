# Activity 9
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 9/30/2022

#1.

# import random
# firstNum=int(random.random()*25)
# secondNum=int(random.random()*25)+25
# 
# while firstNum<=secondNum:
#     firstNum=firstNum+1
#     secondNum=secondNum-1
#     print ("FirstNum:" ,firstNum , "SecondNum:", secondNum)
# 
# print("They have switched places!")

#2.

# def autumnBegins():
#     count=0
#     while count<3:
#         temperature=int(input("Enter low temperature:"))
#         if temperature<45:
#             count=count+1
#         else:
#             count=0
#     print("Autumn has begun!")
# autumnBegins()
# 

#3.
# def loomingStorm():
#     W2=0
#     W1=0
#     while abs(W1-W2)<8:
#         W2=W1
#         W1=int(input("Enter wave heights:"))
#         
#     print("A storm is coming")
# loomingStorm()

#4.
# def candySales():
#     count=0
#     unsoldbars=0
#     soldbars=0
#     Total=0
#     while count<=5:
#         soldbars=int(input("Enter how many candy bars were sold on each day:"))
#         Total=Total+soldbars
#         count=count+1
#         if Total==200 and count==5:
#             return "you did your part for the candy sale!"
#         if Total<200 and count==5:
#             unsoldbars=200-Total
#             return "Sales goal was not met; you must return", unsoldbars,  "unsold bars"
#         if Total==200 and count<5:
#             return "Congratulations, you sold all the candy in only", count, "days"
# print(candySales())
            


    

