import random 
import turtle
import pygame 
import math

#part A
mike = turtle.Turtle()
don = turtle.Turtle()
mike.shape("turtle")
don.shape("turtle")
mike.color("pink")
don.color("navy")
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
window.fill("navy")
pygame.time.wait(500)

side_length = 100
xpos = 300
ypos = 200

sides = [3,4,6,20,100,360]

for sidenum in sides:
    points = []
    for i in range(sidenum):
        angle = 360/sidenum
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])
     
    pygame.draw.polygon(window,"violet", (points))
    pygame.display.flip()
    pygame.time.wait(1500)
    window.fill("navy")


