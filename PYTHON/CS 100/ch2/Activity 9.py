# Activity 9
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 9/14/202#

#1.
#a.
n=10
k=20
print(n>10 and k==20)

#b.
n=10
k=20
print((n==10) and (k==20))

#c.
n=10
k=20
print((n>10) or (k==20))

#d.
n=10
k=20
print((not(n>10) and (k==20)))

#e.
n=10
k=20
print((n>10) or (k==10 or k!=5))

#f.
n=10
k=20
print((not(n>10)) and (not(k==20)))

#g.
n=10
k=20
print((n>10) or (k==10 or k != 5))

#h.
n=10
k=20
print((n<20) or (k==20))

#i.
n=10
k=20
print((n>=10) and (k<=20))

#2.
#a.
num=200
print((num<100 and num>=0)or(num==200))

#b.
num=500
print((num>=0 and num<100))

#c.
num=50
print((num<=150))

#3.
#a.
x=5
y=11
if x>5:
    print("A")
elif y<10:
    print("B")
elif x==10:
    print("C")
else:
    print("D")

#b.
x=10
y=11
if x>5:
    print("A")
elif y<10:
    print("B")
elif x==10:
    print("C")
else:
    print("D")
    
#c.
x=0
y=5
if x>5:
    print("A")
elif y<10:
    print("B")
elif x==10:
    print("C")
else:
    print("D")


#4.

def calccost(numpounds):
    cost=numpounds*0.32
    shipping=7.5
    if numpounds<100:
        shipping=7.5
    else:
        shipping=6
    total=cost+shipping
    return total
print(calccost(300))
#102.0

#5.
def nextnum(num):
    if num%2==0:
        num=num/2
    else:
        num=(num*3)+1
    return num
print(nextnum(15))
#46
        
  
