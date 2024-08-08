import turtle
 
tim=turtle.Turtle()

tim.setheading(0)
tim.width(3)
tim.pencolor("blue")
tim.forward(100)

tim.penup()
tim.forward(100)
tim.pendown()
tim.pencolor("red")
tim.left(90)
tim.forward(100)

def drawThickGreenline():
    tim.pendown
    tim.width(7)
    tim.pencolor("green")
    tim.forward(200)
    
drawThickGreenline()

tim.penup()
x=tim.xcor()
y=tim.ycor()
print(x,y)
tim.goto(x-400,y-400)
tim.pendown()
tim.setheading(270)
drawThickGreenline()
    

