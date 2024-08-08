# Activity 15
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 10/28/2022

numbers=[3,4,0,1,1,2,6,1,8,6,3,1,9,2,9]

# for index in range(len(numbers)):
#     print(numbers[index], end=" ")

#TASK A
def evenSum(evenint):
    sumEven=0
    for index in range(len(evenint)):
        if index%2==0:
            sumEven=sumEven+evenint[index]
    return sumEven
print(evenSum(numbers))

#TASK B
# def CountInlist(integer, numbers):
#     count=0
#     for index in range(len(numbers)):
#         if numbers[index]==integer:
#             count=count+1
#     return count
# integer=9
# print(CountInlist(integer, numbers))
#     
# #TASK C
# def maxInList(numbers):
#     for index in range(len(numbers)):
#         maximumValue=max(numbers)
#     return maximumValue
#         
#                        
# print(maxInList(numbers))
# 
# def maxinlist(numbers):
#     index=0
#     for index in range(len(numbers)):
#         if numbers[index]>numbers[index+1]:
#             index+=1
#         return index
# print(maxinlist(numbers))
#         

#

#TASK D
def swapLocations(num1, num2, numbers):
    temp=numbers[num1]
    numbers[num1]=numbers[num2]
    numbers[num2]=temp
    
swapLocations(6, 4, numbers)
print(numbers)        