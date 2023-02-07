#"float":decimal number, 0,0
#"int": whole number, 1, -1, 0
#"list": a list of things [1,2,3]

#var = 4
#var =input("Enter a number: ")
##to save the number you can do 
#data = input("Enter a number: ")
#print(data, type(data))
##print(data +1) is an error
#data = int(data)
#print(data, type(data))
#print(data + 1)


import random
import math

#always put all your imports first in the file

print(math.pi)

import turtle
#simulates pen and paper
pen1 = turtle.Turtle() #variable = module.function()
pen2 = turtle.Turtle()
pen1.shape("turtle")
pen2.shape("turtle")
pen2.color("purple")
pen1.color("orange")
pen1.speed(1)
pen2.speed(0)
window = turtle.Screen()



pen1.forward(100)
pen1.left(90)
pen1.forward(100)
pen1.left(90)
pen1.forward(100)
pen1.left(90)
pen1.forward(100)
pen1.left(90)
pen1.forward(100)

pen2.forward(50)
pen2.left(60)
pen2.forward(50)
pen2.left(60)
pen2.forward(60)
pen2.left(60)
pen2.forward(50)
pen2.up()
pen2.forward(100)
pen2.down()
pen2.forward(30)

pen2.home()
pen1.goto(0,0)
window.exitonclick() #needs to be last of the turtle

