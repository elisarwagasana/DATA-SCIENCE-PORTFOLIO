import turtle
t=turtle.Turtle()
def compassDirection():
    t.pendown()
    t.setheading(0)
    x=t.xcor()
    y=t.ycor()
    t.goto(x,y)
    t.pendown()
    t.color("black")
    t.width(4)
    t.forward(50)
    t.write("0")
    t.penup()
    t.goto(0,0)
    t.setheading(45)
    t.pendown()
    t.color("black")
    t.width(4)
    t.forward(50)
    t.write("45")
    t.penup()
    t.goto(0,0)
    t.setheading(90)
    t.pendown()
    t.color("black")
    t.width(4)
    t.forward(50)
    t.write("90")
    t.penup()
    t.goto(0,0)
    t.setheading(135)
    t.pendown()
    t.color("black")
    t.width(4)
    t.forward(50)
    t.write("135")
    t.penup()
    t.goto(0,0)
    t.setheading(180)
    t.pendown()
    t.color("black")
    t.width(4)
    t.forward(50)
    t.write("180")
    t.penup()
    t.goto(0,0)
    t.setheading(225)
    t.pendown()
    t.color("black")
    t.width(4)
    t.forward(50)
    t.penup()
    t.forward(20)
    t.pendown()
    t.write("225")
    t.penup()
    t.goto(0,0)
    t.setheading(270)
    t.pendown()
    t.color("black")
    t.width(4)
    t.forward(50)
    t.penup()
    t.forward(20)
    t.pendown()
    t.write("270")
    t.penup()
    t.goto(0,0)
    t.setheading(315)
    t.pendown()
    t.color("black")
    t.width(4)
    t.forward(50)
    t.write("315")
    t.hideturtle()
    
   
compassDirection()

    
    