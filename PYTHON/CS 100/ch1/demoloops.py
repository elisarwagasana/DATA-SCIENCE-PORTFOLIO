# Activity 6 Functions with loops.
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 9/8/2022

#PART 1
#Write code using a for loop to print out the numbers 0 to 10 (0 1 2 3 4 …)
# 
# Write code using a for loop to print out the numbers 0 to 100 by 10s (0 10 20 30 …)
# 
# Write code using a for loop to print out the numbers from -10 to 10 by 2s (-10 -8 -6 …)
# 
# Write code using a for loop to print out the numbers from 10 to 0 (10 9 8 7 …)

#1.
for count in range(0,11):
    print(count)
 
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

#2.
for count in range (0,101,10):
    print(count)
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# 100

#3.
for count in range(-10,11,2):
    print(count)
# -10
# -8
# -6
# -4
# -2
# 0
# 2
# 4
# 6
# 8
# 10

#4.
for count in range(10,-1,-1):
    print(count)
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

#PART 2

#1.
#Draws multiple rectangles
import turtle

t=turtle.Turtle()

def placeRectangle(x,y,height,width):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(90)
    t.forward(height)
    t.right(90)
    t.forward (width)
    t.right(90)
    t.forward (height)
    t.right(90)
    t.forward(width)
 
t.speed('fastest')
t.width(4)
for tall in range(10,100,10):
    placeRectangle(0,0,tall,50)
    
#2.    
def placeRectangle(x,y,height,width):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(90)
    for count in range(4):
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
        
t.speed('fastest')
t.width(4)
x=-100
for tall in range(10,100,10):
    placeRectangle(x,0,tall,50)
    x=x+20
    
#3.    
#The second code changes the output because the x-cordinate is changing (increasing by 20 per rectangle)

#4.
def placeRectangle(x,y,height,width):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(90)
    for count in range(8):
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
        
t.speed('fastest')
t.width(4)
x=-100
for tall in range(10,100,10):
    placeRectangle(x,0,tall,50)
    x=x+20
    
#PART 3
    
#1.    
# Write a drawOctagon function that uses a for loop to draw the octagon instead of eight different sets of turn and forward commands.
# Demonstrate that your new function draws a octagon correctly. (Note: the angle between sides of an octagon is 45 degrees.)

def drawOctagon(side):
    t.pendown()
    t.setheading(0)
    for count in range(8):
        t.forward(side)
        t.right(45)
drawOctagon(100)
    

