# Activity 12
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 10/07/2022

#1.
import random
def squirelAcorns():
    total1=0
    total2=0
    while total1<35 and total2<35:
        collect1=int(random.random()*10)
        total1=total1+collect1
        collect2=int(random.random()*10)
        total2=total2+collect2
        print("Roger got", collect1, "acorns today, now has", total1)
        print("Bernadette got", collect2, "acorns today, now has", total2)
    if total1>35 and total2>35:
        print("They both reached their goal")
    elif total1>35:
        print("Roger reached the goal first")
    else:
        print("Bernadette reached the goal first")
    return total1,total2
   
print(squirelAcorns())


#2.
import random
def portlandtrip():
    totaldistance=0
    count=0
    distanceleft=3186
    print("Day  friend1  Distance left")
    while distanceleft>400:
        distancetravelled=int(random.randint(150,400))
        totaldistance=totaldistance+distancetravelled
        distanceleft=distanceleft-distancetravelled
        count=count+1
        print()
        print(count,"      ", totaldistance,"       ",  distanceleft)
    print()
    print("The friend arrived on day:" , count+1)
    print("They drove", distanceleft, "on the last day")
portlandtrip()
    
        
        
 