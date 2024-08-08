import math
import random
import turtle

# Original version of Monte Carlo Pi 
def montePi(numDarts):
    inCircle = 0       
    for i in range(numDarts):
        x = random.random() # returns a number [0, 1)
        y = random.random()
        d = math.sqrt(x**2 + y**2)   
        if d <= 1:
            inCircle = inCircle + 1
    pi = inCircle/numDarts * 4
    return pi


# Graphic Demonstration version of Monte Carlo Pi
def showMontePi(numDarts):
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.setworldcoordinates(0,0,1,1)

    drawingT = turtle.Turtle()

    # Goto origin and draw horizontal axis
    drawingT.up()
    drawingT.goto(0,0)
    drawingT.down()
    drawingT.goto(1,0)

    # Goto origin and draw vertical axis
    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,0)

    
        # draw upper portion of circle to reduce error
    drawingT.penup()
    drawingT.goto(0,1)
    drawingT.pendown()
    for i in range(45):
        drawingT.forward(6.2831/360)
        drawingT.right(1)
        
    # move turtle to point where the circle intersects the
    # x-axis and point turtle in the upward direction
    drawingT.up()
    drawingT.goto(1,0)
    drawingT.right(225)
    drawingT.down()
    
    # draw the lower portion of the circle to reduce error
    for i in range(45):
        drawingT.forward(6.2831/360)
        drawingT.left(1);
        
    circle = 0
    drawingT.up()
    turtle.tracer(10,1) # tell turtle module to update display quickly

    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        drawingT.penup()
        drawingT.goto(x,y)
        if d <= 1:
            circle = circle + 1
            drawingT.color("blue") # draw inside darts blue
        else:
            drawingT.color("red")  # draw outside darts red
        drawingT.pendown()
        drawingT.dot()
                
    pi = circle/numDarts * 4
    return pi


#print(showMontePi(800))

# Modification to show improving approximation of Pi over time
def showMontePiGraph(numDarts):
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.setworldcoordinates(0,0,2,2)

    drawingT = turtle.Turtle()

    # draw hozinontal axis for plotting darts
    drawingT.up()
    drawingT.goto(0,0)
    drawingT.down()
    drawingT.goto(1,0)

    # draw vertical axis for plotting darts
    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,0)
    
    # draw outer square (upper edge)
    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(1,1)
    drawingT.goto(1,0)
    
    # outer square (right edge)
    drawingT.up()
    drawingT.goto(0,1)
    drawingT.right(0)
    drawingT.down()
    #drawingT.color("green")
    
    # draw upper portion of circle to reduce error
    for i in range(45):
        drawingT.forward(6.2831/360)
        drawingT.right(1)
        
    # move turtle to point where the circle intersects the
    # x-axis and point turtle in the upward direction
    drawingT.up()
    drawingT.goto(1,0)
    drawingT.right(225)
    drawingT.down()
    
    # draw the lower portion of the circle to reduce error
    for i in range(45):
        drawingT.forward(6.2831/360)
        drawingT.left(1);
    
    # draw the axes in the upper right portion of the screen
    drawingT.up()
    drawingT.goto(1,1)
    drawingT.down()
    drawingT.goto(2,1)
    drawingT.up()
    drawingT.goto(1,2)
    drawingT.down()
    drawingT.goto(1,1)
    
    # draw a line in red to indicate where Pi/4 is on the plot
    drawingT.up()
    drawingT.color("red")
    drawingT.goto(1, 1+(3.1415/4))
    drawingT.down()
    drawingT.goto(2, 1+(3.1415/4))
    drawingT.up()

    circle = 0
    drawingT.up()
    turtle.tracer(10,1) # tell turtle module to update display quickly
    
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        drawingT.goto(x,y)
        if d <= 1:
            circle = circle + 1
            drawingT.color("blue")
        else:
            drawingT.color("red")            
        drawingT.dot()
                
        # Cannot draw data before first dart
        if i > 0:
            drawingT.color("black")
            drawingT.up()
            # plot a point indicating the current approximation
            # The "+1" is to put the point in the upper right region
            drawingT.goto((1+i/numDarts), 1+(circle/i))
            drawingT.down()
            drawingT.dot()
            drawingT.up()
        
        
    pi = circle/numDarts * 4
    return pi


#print(montePi(2000))
#print(showMontePi(1500))
print(showMontePiGraph(2000))
