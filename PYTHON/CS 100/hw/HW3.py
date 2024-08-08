# HW3
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 9/16/2022

#1.
def skipSum(start,end,skip):
     sum=0
     n=start
     print("Computing the sum of the following numbers:")
     for value in range(start,end,skip):
         sum=sum+value
         print(value)
     return sum
print("The sum is", skipSum(5,30,3))
#The sum is 153

#2. Write a function called fractionSum() that sums fractions, with a denominator that doubles every time. For example:
#1/1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32 + …

def fractionSum(numTerms):
    sum=0
    sign=1
    denominator=1
    for f in range(numTerms):
        fraction=1/denominator
        sum=sum+(sign*fraction)
        denominator=denominator*2
        print ("Adding" , 1 /denominator , "to the total, which is now:",  sum)
    return sum
print("Final result is :", fractionSum(3))

#3

import turtle
t=turtle.Turtle()

def grid(row,column):
    t.penup()
    t.goto(-300,-200)
    t.pendown()
    for count in range(row):
        t.setheading(0)
        t.forward(row*167)
        t.back(row*167)
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
        t.forward(column*15)
        t.penup()
        t.setheading(90)
        t.forward(column*15)
grid(3,10)

#4.
import turtle
import math

t=turtle.Turtle()
t.speed('fastest')
t.penup()
t.goto(0,300)

# draw circle in the center of the drawing canvas
t.pendown()
t.pencolor("red")
t.width(3)
# This loop draws the "circle" to the screen
# DO NOT CHANGE THIS LOOP IN ANY WAY
for circle in range(361):
    #t.forward(3.0545) <--- this was the value from in class on 9/9/2022
    t.forward(4.9744)
    t.right(1)
    
# add code here to draw the diameter
t.setheading(270)
t.forward(570)
print("Circle's diameter is: ",570)
print("Circle's radius is: ",570/2)
print()

t.pencolor("black")
#draw a square inside the circle
def drawSquare(x,y,side):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for square in range(4):
        t.forward(side)
        t.right(90)
drawSquare(200,210,400)
print("Inner Square's side is: ",400) 
print("Inner Square's perimeter is: ",400*4)
print()

#draw a square outside the circle
def drawSquare(x,y,side):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for square in range(4):
        t.forward(side)
        t.right(90)
drawSquare(290,300,575)
print("Outer Square's side is: ",575)
print("Outer Square's perimeter is: ",4*575)
print()

print("The inner perimeter and outer perimeter are lower and upper bounds for the circumference")
print()
print("Therefore, the Circle's circumference is greater than ", 400*4, " and less than ", 575*4)
print()

circumference = (1600 + 2300)/2
print("As an approximation, we'll use a value half between: ", circumference)
print("The formula for a circle's 'perimeter' is: Circumference = 2*Pi*Radius")
print("Solving for Pi yields: Pi = Circumference / (2*Radius)")
print()
piApprox = circumference / (2 * 285)
print("to calculate Pi: ", piApprox)
print()
print("The difference from the actual value of Pi is: ", piApprox - math.pi)

#5.

def archimedesPiApprox(numsides):
    #circApprox = (numsides * 2 * math.sin(math.radians(360/(2*numsides))))
    circApprox= (numsides * 2 * math.tan(math.radians(360/2*numsides)))
    piApprox = circApprox / 2
    return piApprox
print(archimedesPiApprox(200))
#CPiApprox using sin= 3.1416
#PiApprox using tan= 7.857546894913888e-13

def archimedesPiApprox(numsides):
    circApprox1= (numsides * 2 * math.sin(math.radians(360/(2*numsides))))
    circApprox2= (numsides * 2 * math.tan(math.radians(360/2*numsides)))
    piApprox= (circApprox1+circApprox2)/2
    return piApprox
print(archimedesPiApprox(200))

#c.
#Pi approxinmation of the inside polygon works for all number of sides to get the value of pi and when we add
#the inner and outer approxinmations, we can use it for all number of sides to return the value of pi. However, pi approximation
#of the outer polygon can't work alone to get the value of pi.




    
