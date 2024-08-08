#HW2
# 
# Author: Elisa Rwagasana Ishimwe  2(11AM)
# 
# Date: 9/7/2022

### Question 1
### Write a function called carpetCalculation() that takes three parameters: length of room in feet, 
### width of room in feet and cost of carpet in dollars per square yard. The function should calculate the cost of carpet 
### for the room and print the results. Note: 1 yard = 3 feet, 1 square yard = 9 square feet.

def carpetCalculation(length,width,costpersquareyard):
    areaInSquareYard=(length*width)/9
    y=costpersquareyard*(length*width)/9
    return y

thecost = carpetCalculation(50,30,5)

print(thecost)
#833.3333333333334

### Question 2
### Write a function called normanWindowArea() that takes in two parameters the height of the window and the radius of the 
### circular portion and calculates the area (amount of glass needed for the Norman window). The height is the longer dimension 
### of the rectangular portion of the window.
### see link for an example of a Norman window.

import math
print(math.pi)

def normanWindowArea(height,radius):
    areaOfTheRectangularPortionOfTheWindow=2*radius*height
    areaOfTheSemiCircularPortion=(math.pi*radius**2)/2
    a=areaOfTheRectangularPortionOfTheWindow+areaOfTheSemiCircularPortion
    return a
theArea=normanWindowArea(60,20)
print(theArea)
#3028.3185307179588

### Question 3
### Write a function called tree() that draws a stick figure tree (use your creativity, but it must have at least 
### four lines in it). The function should have two parameters: the x location of the tree and the y location of 
### the tree. Write another function called forest() that has no parameters and it draws 7 trees in different 
### locations by calling the tree() function 7 times.

import turtle
t=turtle.Turtle()
print("orig.pos:", t.position())
t.setheading(0)
t.pendown()
x=t.xcor()
y=t.ycor()
print(x,y)

def tree(x,y):
    t.penup()
    t.goto(x,y)
    t.setheading(270)
    t.pendown()
    t.forward(100)
    t.setheading(90)
    t.forward(100)
    t.penup()
    t.setheading(45)
    t.pendown()
    t.forward(100)
    t.penup()
    t.back(100)
    t.setheading(10)
    t.pendown()
    t.forward(100)
    t.penup()
    t.back(100)
    t.setheading(135)
    t.pendown()
    t.forward(100)
    t.penup()
    t.back(100)
    t.setheading(170)
    t.pendown()
    t.forward(100)
#tree(100,100)

def forest():
    tree(-50,200)
    tree(-150,100)
    tree(200,-120)
    tree(-250,-230)
    tree(80,-100)
    tree(-300,100)
    tree(-30,-180)
# forest()


### Question 4
### Write a function called drawHouse(). Use the functions that we have written in class to draw 
### Rectangles and Triangles. Have the new function draw a house using at least two triangles 
### and at least three rectangles. Your house should have multiple colors and multiple line thicknesses.

def drawHouse():
    t.setheading(0)
    t.penup()
    t.goto(150,100)
    t.pendown()
    t.color("purple")
    t.width(7)
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.setheading(0)
    t.penup()
    t.goto(230,-20)
    t.pendown()
    t.pencolor("pink")
    t.width(6)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.pencolor("yellow")
    t.width(5)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.back(30)
    t.setheading(140)
    t.color("orange")
    t.width(4)
    t.forward(30)
    t.setheading(215)
    t.forward(35)
    t.penup()
    t.goto(150,100)
    t.setheading(45)
    t.pencolor("green")
    t.width(3)
    t.pendown()
    t.forward(150)
    t.setheading(313)
    t.forward(143)
# drawHouse()
    
### Question 5
### Write a function called grid() that draws a 6x6 grid with black lines outlining each square. To draw this properly, 
#you will need 7 vertical lines and 7 horizontal lines. You MUST use loops for this function. Extra challenge: Write the method 
### so that it takes two parameters, the number of rows and the number of columns in the grid.    

def grid(row,column):
    t.penup()
    t.goto(-350,-300)
    t.pendown()
    for count in range(row):
        t.setheading(0)
        t.forward(row*50)
        t.back(row*50)
        t.penup()
        t.setheading(90)
        t.pendown()
        t.forward(50)
    for count in range(column):
        t.penup()
        t.setheading(0)
        t.pendown()
        t.forward(50)
        t.setheading(270)
        t.forward(column*50)
        t.penup()
        t.setheading(90)
        t.forward(column*50)
#grid(6,6)
    
    
        
    
    
    
    
    

    
    
    


    





    
    
    
    
    
    
    
