# Activity 16
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 11/02/2022

# numbers=[3,4,0,1,1,2,6,1,8,6,3,1,9,2]
# numbers=[1,2,3,8,10]


#TASK A

# def histogram(list):
#     for num in list:
#         print(num, "", end=" ")
#         for ch in range(num):
#             print('#', end="")
#         print()
# 
# histogram(numbers)

#TASK B

def balanceList(numbers):
    print(numbers, end=" ")
    length=len(numbers)
    if length%2==0:
        half=length//2
        half1=numbers[half:]
        half2=numbers[:half]
        sum1=sum(half1)
        sum2=sum(half2)
        if sum1==sum2:
            return True
        else:
            return False
    else:
        return False
# print(balanceList(numbers))
#     

             
#TASK C

def increasing(list):
    index=0
    for ch in range(len(list)-1):
        if list[index]>=list[index+1]:
            return False
        index+=1
       
    return True
    
    
# print(increasing(numbers))
#     

    
    
    
        
        
    