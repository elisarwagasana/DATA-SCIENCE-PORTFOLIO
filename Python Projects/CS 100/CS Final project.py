import turtle
import random


t = turtle.Turtle()
q = turtle.Turtle()
s= turtle.Turtle()
#this function draws he room for the level and takes two parameters: the color of the room and prints the level 
def drawRooms(color, level):
    t.penup()
    t.goto(328,332)
    t.pendown()
    t.color('black')
    t.width(13)
    turtle.bgcolor(color)
    t.speed('fastest')
    t.setheading(0)
    for i in range(4):
        t.right(90)
        t.forward(660)
    t.penup()
    t.goto(280,300)
    t.pendown()
    t.width(5)
    t.write(level)

#This function draws a compass on the screen so that the player can have a sence of direction.
def compassDirection():
    s.penup()
    s.goto(-280,-280)
    s.pendown()
    s.color('black')
    s.width(3)
    for val in range (8):
        s.forward(25)
        s.backward(25)
        s.right(45)

    s.penup()
    s.goto(-250,-290)
    s.pendown()
    s.write('0')
    s.penup()
    s.goto(-265,-265)
    s.pendown()
    s.write('45')
    s.penup()
    s.goto(-290,-255)
    s.pendown()
    s.write('90')
    s.penup()
    s.goto(-320,-265)
    s.pendown()
    s.write('135')
    s.penup()
    s.goto(-320,-290)
    s.pendown()
    s.write('180')
    s.penup()
    s.goto(-315,-310)
    s.pendown()
    s.write('225')
    s.penup()
    s.goto(-290,-315)
    s.pendown()
    s.write('270')
    s.penup()
    s.goto(-265,-315)
    s.pendown()
    s.write('315')
    
        
   
   
   
   
    
   

      
#this function makes the turtle move based on what the player inputs, this is not working and needs to be fixed     
def turtleMoving():   
    totalDistance = 0
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.shape('turtle')
    t.speed('normal')
    t.color("black")
    while totalDistance <= 2000:
        direction = int(input("Enter direction:", ))
        distance =int( input("Enter distance:", ))
        t.pendown()
        t.width(3)
        t.setheading(direction)
        t.forward(distance)
        totalDistance = totalDistance + distance
    
    
# This function makes the location of the escape in a random location, and takes 2
# parameters: width and color. The width is how wide the escape is and color is the color of the sqaure.
def escape(width,color):
    x = random.randint(-300,203) 
    y = random.randint(-207,300) 
    while((x > -130) and (x < 150)) and ((y > -130) and (y < 150)):
        x = random.randint(-300,203) 
        y = random.randint(-207,300) 
    q.penup()
    q.hideturtle()
    q.goto(x,y)
    q.pendown()
    q.pencolor(color)
    q.width(3)
    q.setheading(0)
    q.pendown()
    for count in range(4):
        q.forward(width)
        q.right(90)
    
    totalDistance = 0
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.shape('turtle')
    t.speed('normal')
    t.color("black")
    escaped = False
    while totalDistance <= 2000 and escaped == False and ((t.xcor() < 328) and (t.xcor() > -332) and ( t.ycor() < 332) and (t.ycor() > -328)) :
        direction = int(input("Enter direction:", ))
        distance =int( input("Enter distance:", ))
        t.pendown()
        t.width(3)
        t.setheading(direction)
        totalDistance = totalDistance + distance
        if totalDistance > 2000:
            print( "You have traveled too far :(")
        for travel in range(distance):
            t.forward(1)
            if (t.xcor() > x) and (t.xcor() < x + width) and (t.ycor() < y) and (t.ycor() > y - width):
                escaped = True
            if (t.xcor() >= 328) and (t.xcor() <= -332) and ( t.ycor() >= 332) and (t.ycor() <= -328): 
                print("You lost because you ran into a wall :(") 
                
    
    if escaped == True:
        print("The turtle has escaped!")

drawRooms('light blue','level 1')
compassDirection()
print("This a game where you want to help the turtle escape a room. To do this it needs to find an invisable trap door. How to play is you will enter a direction (0-359). After this you will enter a distance. The ways that you can lose is either traveling more than 2000 units or running into the wall. If you find the escape you will move onto the next level.")  
escape(125,"light blue")
t.clear()
q.clear()
print()
print()
print()

drawRooms('plum','level 2')
print("If you have escaped the room move onto Level 2")  
escape(100,"plum")
t.clear()
q.clear()
print()
print()
print()

drawRooms('light green','level 3')
print("If you have escaped the room move onto Level 3")  
escape(75,"light green")     




    
    
    
    


    
    



     
    
    
    

