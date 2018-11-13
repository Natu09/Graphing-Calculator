from SimpleGraphics import *
from math import *

# Graphing Calculator
# Nathaniel Habtegergesa
# 30051338
# To be able to graph mathematical expressions  

# Set Background Colour

background ("white")

# getting rid of magic numbers 

width = 400
width_2 = 30
length = 300

# my x and y axis 

line (0, length, 799, length)
line (width, 0, width, 599)

# create a loop that will draw the x axis   

for x_pos in range (1,14,1):
    line (width + width_2 * x_pos, 310,width + width_2 * x_pos, 290)
    setFont ("Times", "12", "bold") 
    text (width + width_2 * x_pos, 320, x_pos )

for x_neg in range (-13, 0, 1):
    line (width + width_2 * x_neg, 310, width + width_2 * x_neg, 290)
    setFont ("times", "12", "bold" ) 
    text (width + width_2 * x_neg, 320, x_neg)

# create a loop that will draw the y axis

for y_neg in range (-10, 0, 1):
    line (390, length - width_2 * y_neg, 410, length - width_2 * y_neg)
    setFont ("times", "12", "bold" ) 
    text (420, length - width_2 * y_neg, y_neg)

for y_pos in range (1, 11, 1):
    line (390, length - width_2 * y_pos, 410, length - width_2 * y_pos)
    setFont ("times", "12", "bold" ) 
    text (420, length - width_2 * y_pos, y_pos)

# getting input/output

expression = input("Enter an arithmetic expression: \n y = ") 
x = -13
count = 0

# Making lines different colors using while loops and if statements

while expression != "": 
    if count%3 == 0:
            setColor ("red")
    elif count%3 == 1:
            setColor ("green")
    else:
            setColor ("blue")
            
    while x >= -13 and x <= 13:
        y_coord = eval(expression)
        x = x + 0.1
        x2 = x
        y2_coord = eval(expression)
        x = x - 0.1
        line (x * width_2 + width , y_coord * - width_2 + length, (x+0.1) * width_2 + width,y2_coord * - width_2 + length)

# Max and Mins

        current_y = eval(expression)
        x = x + 0.1
        next_y = eval(expression)
        x = x - 0.2
        last_y = eval(expression)
        x = x + 0.1
        current_slope = (next_y - current_y)
        last_slope = current_y - last_y
        if( current_slope * last_slope < 0):
            if (last_slope < 0):
                setColor("orange")
            else:
                setColor("purple")
            ellipse (x * width_2 + width , y_coord * - width_2 + length, 5, 5)
        if count%3 == 0:
            setColor ("red")
        elif count%3 == 1:
            setColor ("green")
        else:
            setColor ("blue")
                    
        x = x + 0.1            
    expression = input("Enter an arithmetic expression: \n  y = ")
    count = count + 1
    x = -13

# closes the program when a blank space is entered 

close() 
