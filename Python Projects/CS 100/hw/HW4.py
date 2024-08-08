# HW4
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 9/28/2022

import turtle
t=turtle.Turtle()
import random

#1.
def numberDescription(a):
    if int(a)==a:
        if a>0:
            print("positive integer")
        else:
            print("negative integer")
    if not(int(a))==a:
        if a>0:
            print("positive decimal")
        else:
            print("negative decimal")
#numberDescription(-21)
            
    
#2.
def randomPolygon(numsides):
    startx=t.xcor()
    starty=t.ycor()
    t.pendown()
    t.setheading(0)
    #numsides=numsides-1
    for count in range(numsides-1):
        x=int((random.random()*600) - 300)
        y=int((random.random()*600) - 300)
        t.goto(x,y)
    t.goto(startx,starty)
#randomPolygon(3)

#3.
def checkThree(a,b,c):
    if a==b and b==c:
        print("All three values are the same")
    elif a==b or b==c or a==c:
        print("Two of the values are equal")
    elif a>b and a<c or a>c and a<b:
        print("All three values are different and the middle value is:", a)
    elif b>a and b<c or b>c and b<a:
        print("All three values are different and the middle value is:", b)
    else:
        print("All three values are different and the middle value is:", c)

#checkThree(7,7,7)
#checkThree(8,3,8)
#checkThree(0,0,5)
#checkThree(2,9,12)
#checkThree(4,1,9)
#checkThree(2,20,17)
    

#4.
def twoBoxDots(num):
    t.penup()
    t.goto(200,200)
    t.pendown()
    t.setheading(0)
    for count in range(4):
        t.forward(150)
        t.right(90)
    t.penup()
    t.goto(-200,200)
    t.pendown()
    for count in range(4):
        t.forward(150)
        t.right(90)
    inBox1=0
    inBox2=0
    outsideBox=0
    for dots in range(num):
        x = int((random.random()*600) - 300)
        y = int((random.random()*600) - 300)
        
        if x>200 and x<350 and y>50 and y<200:
            t.pencolor("green")
            inBox1=inBox1+1
        elif x>-200 and x<-50 and y>50 and y<200:
            t.pencolor("red")
            inBox2=inBox2+1
        else:
            t.pencolor("blue")
            outsideBox=outsideBox+1
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.width(10)
        t.setheading(0)
        t.pendown()
        t.forward(1)
        
    print("In box 1:" ,inBox1)
    print("In box 2:" ,inBox2)
    print("Out of both boxes",outsideBox)

t.speed("fastest")
twoBoxDots(100)        

    




        
    
    
    