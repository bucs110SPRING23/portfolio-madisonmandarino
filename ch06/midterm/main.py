import turtle
import random

window = turtle.Screen()
window.bgcolor('dark blue')
pen  = turtle.Turtle()

def stars():
    pen.speed(7)
    star_color = "yellow"
    star_location_height = 400
    star_location_width = 400
    pen.color(star_color)
    for star in range(600):
        pen.up()
        x = random.randint(-star_location_width, star_location_width)
        y = random.randint(-star_location_height, star_location_height)
        star_size = random.random()*4
        pen.goto(x,y)
        pen.dot(star_size)
    pen.speed(2)

def moon():
    pen.up()
    pen.goto(-300,225)
    pen.color('yellow')
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()
    pen.up()
    pen.goto(-275,250)
    pen.color('dark blue')
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

def buildings():
    pen.up()
    pen.goto(-360,-330)
    building_heights = [250,300,225,175,350,225,180,90,110]
    for height in building_heights:
        pen.down()
        pen.color('black')
        pen.begin_fill()
        pen.left(90)
        pen.forward(height)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
        pen.forward(height)
        pen.end_fill()
        pen.left(90)
        pen.forward(1)

stars()
moon()
buildings()

pen.hideturtle()
window.exitonclick()



