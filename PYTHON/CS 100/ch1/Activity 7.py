#1
def sumOfTheFirst50():
    sum=0
    n=1
    for iter in range(50):
        sum=sum+n
        n=n+1
    return sum
print (sumOfTheFirst50())
       


import turtle

t=turtle.Turtle()

t.speed('fastest')

# This function draws a polygon with a parameter specified number of sides
def drawPolygon(numSides):
     t.setheading(90)
     t.penup()
     t.goto(-300,0)
     t.pendown()
     for sides in range(numSides):
         t.forward(50)
         t.right(360/numSides)
for p in range(3,31):
         drawPolygon(p)

import math 
def archimedesOctagon():
      side = 2 * math.sin(math.radians(45/2.0))
      polygonCircumference = 8 * side
      return (polygonCircumference / 2)
print(archimedesOctagon())

def archimedesDecagon():
      side = 2 * math.sin(math.radians(36/2.0))
      polygonCircumference = 10 * side
      return (polygonCircumference / 2)
print(archimedesDecagon())

def archimedesPiApprox(numsides):
    circApprox = (numsides * 2 * math.sin(math.radians(360/(2*numsides))))

    piApprox = circApprox / 2
    return piApprox

print("Pi with 250 sides: ", archimedesPiApprox(250))

def archimedesPiApprox(numsides):
        circApprox = (numsides * 2 * math.sin(math.radians(360/(2*numsides))))

        piApprox = circApprox / 2
        return piApprox
for p in range(3,251):
    print("Pi with ",p," sides: ", archimedesPiApprox(p))

    