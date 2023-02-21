import random 
import turtle
import pygame 
import math

#part A
mike = turtle.Turtle()
don = turtle.Turtle()
mike.shape("turtle")
don.shape("turtle")
mike.color("red")
don.color("blue")
mike.up()
don.up()
mike.goto(-100,20)
don.goto(-100,-20)
window = turtle.Screen()
a = random.randrange(1,100)
b = random.randrange(1,100)
mike.down()
don.down()

#race 1 
mike.forward(a)
don.forward(b)
mike.up()
don.up()
mike.goto(-100,20)
don.goto(-100,-20)
mike.down()
don.down()

#race 2
for _ in range(1):
    mike.forward(a)
    don.forward(b)
    print(a)
    print(b)
    mike.up()
    don.up()
    mike.goto(-100,20)
    don.goto(-100,-20)
    mike.down()
    don.down()
    mike.clear()
    don.clear()

window.exitonclick()

#part b
pygame.init()
window = pygame.display.set_mode()
window = fill("green")
pygame.display.flip()
