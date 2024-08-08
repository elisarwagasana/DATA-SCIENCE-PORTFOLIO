# This program is the culmination of our discussion of the Collatz Conjecture
# Now that we have WHILE loops in our toolbelt, we can actually write a
# program to do the Hailstone number calculation! This version of the program
# is partially complete, and we will put the finishing touches on it in class
#
# Author: D. Palmer
#
# Date: October 2, 2022
#
# Modified by: <Elisa Rwagasana Ishimwe> October 3, 2022

import turtle

# Get the hailstone number before opening the drawing canvas
print("Enter a hailstone number: ")
hail = int(input("Enter a hailstone number:"))

t = turtle.Turtle()
wn = turtle.Screen()
# reset the drawing canvas coordinates to be from 0 to 1
wn.setworldcoordinates(0,0,1,1)
t.speed("fastest")

# Draws the X and Y axes of the plot.
def drawAxes():
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.width(2)
    t.goto(0,1)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.goto(1,0)

# This function allows quick scaling of the plot to handle a wider range of values
def scale(num):
    return num/1000

# This function should return the next hailstone number after the one in the parameter
def hailstoneNum(num):
    if num%2==0:
        num=num/2
    else:
        num=(num*3)+1
    return num

# This function plots the sequence of hailstone numbers on a graph
#
# You will need to augment this function to calculate the largest
# value the the hailstone sequence reaches, and the number of steps
# it takes to reach the number 1
def hailstonePlot(num):
    x = 0
    y = scale(num)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.pencolor("GREEN")
    print("To be completed")
    
    # This while loop will do the core calculation to
    # compute the next hailstone number in a loop
    # until the sequence is completed
    #
    # You will need to uncomment this code and
    # provide a boolean expression for the while loop
    # so that the calculation will be correct.
    steps=0
    maxvalue=0
    while num>1 :
        x = x + 0.008 # shift along the x-axis
        num = hailstoneNum(num)
        steps=steps+1
        if num<1:
            steps=0
        if num>maxvalue:
            maxvalue=num
            
        
        t.goto(x,scale(num)) # draw the line on the graph
    return maxvalue,steps

        
drawAxes()
#hailstonePlot(hail) # this line will be commented out
print("Max value and num steps: ", hailstonePlot(hail)) #<-- this line will be uncommented

# You will need to modify this program in several ways:
#
# Step 1: Uncommented the code in the function hailstonePLot
# Step 2: Provide the correct boolean expression for the while loop
# Step 3: Run the program and see the results
# Step 4: Write the function hailstoneNum()
# Step 5: Run the program again and see the results
#
# Verify that you have the program running and plotting correctly
#
# Step 6: Add code to the function hailstonePlot() to count how many steps to reach 1
# Step 7: Run the program and verify the number of steps for the values in the table
# Step 8: Run the program and caluclate the number of steps for the three final values
#
# Step 9: Add code to the function hailstonePlot() to find the largest value in the sequence
# Step 10: Run and verify the values in the table
# Step 11: Run and calculate the maximum values for the three final numbers in the table
#
# Step 12: Submit this In-Class activity program to Moodle
#
# The maximum value that the hailstone number sequence reaches
# -and-
# The total number of steps it takes to reach the value 1
#
# Some examples:    hailstone number        Max value     Num Steps
#                             7             52            16
#                            11             52            14
#                            23            160            15
#                           101            304            25
#                           131            592            28
#
# Once it works            2001            6004           50
# Fill in the rest           27            9232           111
# of this table            1401            45520          96