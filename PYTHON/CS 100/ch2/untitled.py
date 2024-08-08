import turtle
import random
#From time import *

t = turtle.Turtle()

#this function draws he room for the level and takes two parameters: the color of the room and prints the level 
def drawRooms(level):
    turtle.bgcolor("black")
    #t.hideturtle()
    t.penup()
    t.goto(328,332)
    t.pendown()
    t.width(13)
    t.speed('fastest')
    for i in range(4):
        t.right(90)
        t.forward(660)
    t.penup()
    t.goto(280,300)
    t.color("white")
    t.pendown()
    t.width(5)
    t.write(level)
    t.width(50)
   
    
drawRooms('level 1') #how to get the level to come off the turtle screen?
# t.clear()
#drawRooms('plum','level 2')
# t.clear()
#drawRooms('light green','level 3')
# t.clear()

      
#this function makes the turtle move based on what the player inputs
def turtleMoving():   
    totalDistance = 0
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.shape('turtle')
    t.speed('normal')
    t.color("white")
    while totalDistance <= 2000:
        direction = int(input("Enter direction:", ))
        distance =int( input("Enter distance:", ))
        t.pendown()
        t.width(3)
        t.setheading(direction)
        t.forward(distance)
        totalDistance = totalDistance + distance

# This function makes the location of the escape in a random location, and takes 2
# parameters: x and y. The x is how wide the escape is and y is how tall it is.
def escape(width,color):
    x = random.randint(-300,300) 
    y = random.randint(-300,300) 
    x = random.randint(-300,203) 
    y = random.randint(-207,300) 
    while((x > -130) and (x < 150)) and ((y > -130) and (y < 150)):
        x = random.randint(-300,203) 
        y = random.randint(-207,300) 

    t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.pencolor('light blue')
    t.width(3)
    t.setheading(0)
    t.pendown()
    for count in range(4):
        t.forward(width)
        t.right(90)
#create the turtle
    count = Turtle()
    count.speed(0)
    count.penup()
    count.goto(0,260)
    count3=0

#this is the loop
    for count2 in range(10):#replace the 10 with the number you want to count from
        count3 = 10 - count2
        count.clear()
        count.write(count3, align="center", font=("arial", 24, "normal"))
        sleep(1)



        
escape(150,color)
     

def thingsThatStop():
    if (x > 328) or (x < -332) or ( y > 332) or (y < -328): 
        print(" You have lost because you ran into a wall")
    if totalDistance > 2000:
        print( "You have traveled too far")
