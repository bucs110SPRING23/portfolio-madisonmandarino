import turtle
import random

window = turtle.Screen()
turt = turtle.Turtle()

in_window = True

while in_window:
    coinflip = random.randint(0,2)
    if coinflip == 1:
        turt.left(90)
    else: 
        turt.right(90)
    turt.forward(50)

turt_xcords = window.window_width()/2
turt_ycords = window.window_height()/2
if abs(turt.xcords()) > turt_xcords or abs(turt.ycords()) > turt_ycords:
    in_window = False

window.exitonclick()