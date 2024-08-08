# Review questions
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 9/19/2022

#1.
a = 10
b = 9
c = 2
d = a + b + c
print (a)
print (b)
print (c)
print (d)

#2
a = 10
b = 3
c = a / b #normal division
d = a // b #division but you round it down (no decimals)
print (a)
print (b)
print (c)
print (d)

#3.
a = 100
b = a % 10 #(% finding remainder)
c = a % 30
d = a % 44
print (a)
print (b)
print (c)
print (d)

#4.
a = 20
b = 11
a = b
c = a
d = b
print (a)
print (b)
print (c)
print (d)

#5.





#FUNTIONS
#1.
def func1(num):
    result = num*num + num
    print(result)
func1(7)
#56

#2.
def calculate(value1, value2):
    if value1 == value2:
        total = 0
    elif value1 > value2:
        total = value1*value1-value2*value2
    else:
        total = value2*value2-value1*value1
    return total
print(calculate(10, 5))
#75

#3.
import turtle
t=turtle.Turtle()

def drawStuff(num):
    t.penup()
    x=t.xcor()
    y=t.ycor()
    t.pendown()
    for iter in range(num):
        t.setheading(90)
        t.forward(50)
        t.setheading(0)
        t.forward(50)
    t.setheading(270)
    t.forward(num * 50)
    t.goto(x,y)
t.penup()
t.goto(0,0)
drawStuff(5)

def func1(num):
    return (3 * num) + 1
def func2(val1, val2):
    return func1(val1) + func1(val2)

print(func2(4, 11))
#41

#loops
#4.
# import random
# value=100
# for i in range(10):
#     rand=int(random.randon()*9)+1
#     value=value-rand
#     print (value)
#     
# 
def doubleList(numTerms):
    n=1
    for iter in range(numTerms):
        print(n, end=" ")
        n=n*2
    print()
doubleList(3)
doubleList(10)


def trend(num1,num2,num3):
    if num1<num2 and num2<num3:
        print("The numbers are increasing")
    elif num1>num2 and num2>num3:
        print("The numbers are decreasing")
    else:
        print("The numbers are neither increasing nor decreasing")
trend(40,18,28)



def coordinates(x,y):
    if x%2==0 and y%2==0:
        print("Both numbers are even")
    elif x%2==1 and y%2==1:
        print("Both numbers are odd")
    elif x%2==0 and y%2==1:
        print("The first is even and the second is odd")
    else:
        print("The first is odd and the second is even")
coordinates(10,-5)


import turtle
t=turtle.Turtle()

def drawSquare(side,color):
    x=t.xcor
    y=t.ycor
    t.setheading(0)
    t.pendown()
    t.pencolor(color)
    t.width(5)
    for x in range(4):
        t.forward(side)
        t.left(90)
color="red"
numSquares=6

for count in range(numSquares):
    side=(count+1)*20
    drawSquare(side,color)
    
    if color=="red":
        color="blue"
    else:
        color="red"

        





