for count in range (11):
    print(count)
for count in range (11):
    print("hello person number:",count)

import turtle
t=turtle.Turtle()
def drawSquareLoop(side):
    t.pendown()
    t.setheading(0)
    for count in range(4):
        t.forward(side)
        t.right(90)
t.width(5)
# drawSquareLoop(50)

def drawSpiral():
    t.pendown()
    t.setheading(0)
    for count in range(15,200,10):
        t.forward(count)
        t.right(90)
t.speed('fastest')
t.width(5)
drawSpiral()
    