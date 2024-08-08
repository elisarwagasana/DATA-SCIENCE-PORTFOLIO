# Activity 10
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 9/19/2022

import turtle
import random
#1.
# This function draws the coordinate axes using a loop
def drawAxes():
    head = 0
    t.width(4)
    for dir in range(4):
        t.pendown()
        t.setheading(head)
        t.forward(300)
        t.penup()
        t.goto(0,0)
        head = head + 90
        
# This function draws 10 random red dots on the canvas
# students are tasked with counting how many in each quadrant
def drawRandomDots():
    # Initializes all the count variables
    northEastCount = 0
    northWestCount = 0
    southEastCount = 0
    southWestCount = 0
    for dots in range(10):
        x = int((random.random()*600) - 300)
        y = int((random.random()*600) - 300)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.pencolor("red")
        t.width(10)
        t.setheading(0)
        t.pendown()
        t.forward(1)
        if x>0 and y>0:
            northEastCount=northEastCount+1
        elif x<0 and y>0:
            northWestCount=northWestCount+1
        elif x>0 and y<0:
            southEastCount=southEastCount+1
        else:
            southWestCount=southWestCount+1
            
    print("There are ", northEastCount, " dots in the Upper Right Quadrant")
    print("There are ", northWestCount, " dots in the Upper Left Quadrant")
    print("There are ", southEastCount, " dots in the Lower Right Quadrant")
    print("There are ", southWestCount, " dots in the Lower Left Quadrant")
t = turtle.Turtle()
t.speed("fastest")
#drawAxes()
#drawRandomDots()
    
#2.
import turtle
import random

# This function draws a 400 by 400 square in the middle of the canvas
# Students must write this code using a loop
def drawBox():
    t.penup()
    t.goto(0,0)
    t.pendown()
    for square in range(4):
        t.forward(300)
        t.right(90)
#drawBox()
    
# to be written by students
 
# This function draws 10 random red dots on the canvas
# students are tasked with counting how many are inside the box
# and how many are outside the box
def drawRandomDots(num):
    # Initializes all the count variables
    insideBox = 0
    outsideBox = 0

    for dots in range(num):
        x = int((random.random()*600) - 300)
        y = int((random.random()*600) - 300)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.pencolor("red")
        t.width(10)
        t.setheading(0)
        t.pendown()
        t.forward(1)
        # Add a conditional statements here that correctly counts
        # the dots inside and outside the box
        if x>0 and y<0:
            insideBox=insideBox+1
        else:
            outsideBox=outsideBox+1
    print("There are ", insideBox, " dots in the box")
    print("There are ", outsideBox, " dots outside of the box")

t = turtle.Turtle()
t.speed("fastest")
drawBox()
drawRandomDots(50)

#3.


def getMax(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print( getMax(7, -4, 99) )
print( getMax(23, 5, 0) )
print( getMax(17, 74, 9) )
print( getMax(7, 7, -9) )
print( getMax(2, 2, 2) )
print( getMax(7, 9, 9) )
print( getMax(9, 7, 9) )
