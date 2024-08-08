# Activity 4 Functions with Parameters
#
# This program demonstrates writing and calling functions with parameters
#by drawing shapes with different characteristics to the graphics canvas.
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 9/5/2022
#
import turtle
t=turtle.Turtle()

def fixedSquare():
    t.pendown()
    t.setheading(0)
    x=t.xcor()
    y=t.ycor()
    t.goto(x,y)
    t.pendown()
    t.width(4)
    t.forward(75)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(75)

#This funtion draws a square of size 75 at the current location of the turtle 
fixedSquare()
t.penup()
t.goto(50,50)
fixedSquare()

#This funtion draws a square of size 100 at the current turtle's location 
def customSquare(side):
    t.pendown()
    t.width(4)
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.right(90)
    t.forward(side)
customSquare(100)
t.penup()
t.goto(-90,60)
t.pendown()
customSquare(250)

#This function calls a rectangle with height of 50 pixels and width of 150 pixels
def customRectangle(height, width):
    t.penup()
    t.goto(60,-60)
    t.pendown()
    t.width(4)
    t.setheading(0)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
customRectangle(50,150)
t.penup()
t.goto(80,80)
t.pendown()
customRectangle(30,60)

#This function draws a rectangle at (-100,100) with a height of 75 pixels and width of 200 pixels
def placeRectangle(x, y, height, width):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.width(4)
    t.setheading(0)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
placeRectangle(-100,100,75,200)
t.penup()
t.goto(-150,-150)
t.pendown()
placeRectangle(-150,-150,50,150)

#This function calls a red rectangle at (10,50) with a height of 100 pixels and width of 175 pixels
def userRectangle(x,y,height,width,thickness,hue):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.width(thickness)
    t.pencolor(hue)
    t.setheading(0)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
userRectangle(10,50,100,175,10,"red")
t.penup()
t.goto(180,180)
t.pendown()
userRectangle(180,180,80,150,5,"blue")
    
    
    
    
    
  
     


    
    


