# import random
# def randRangeCount(num):
#     count=0
#     for val in range(num):
#          rand = int(random.random()*100)
#          print(rand)
#          if rand >= 25 and rand < 50:
#              count = count + 1
#     return count
# print("There were ", randRangeCount(20), " values of 20 generated in the range 25-50")
# 
# 
# def randomRangeCount2(num):
#     count=0
#     generated=0
#     while count<num:
#         rand=int(random.random()*100)
#         generated=generated+1
#         print(">>>", rand)
#         if rand >=25 and rand<50:
#             count=count+1
#     return generated
# 
# print()
# print(randomRangeCount2(10), "random values were generated to get 10 in the range 25-50")

def frisbeeThrows():
    numThrows=0
    average=0
    sum=0
    while average<=150:
#         print("Please enter the distance of the throw:")
        distance=int(input("Please enter the distance of the throw:"))
        
        numThrows=numThrows+1
        sum=sum+distance
        average=sum/numThrows
        
        print("Congrants! you reached your goal of 150 meters average")
        print("Your average was:", average)
    return numThrows
print("It took", frisbeeThrows(), "throws to average 150 meters")
    