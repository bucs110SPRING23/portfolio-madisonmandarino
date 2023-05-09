import turtle
num_sides = int(input("How many sides do you want to draw?: "))
length_sides = int(input("How long is each side?: "))
angle=(360/num_sides)
print(angle)

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape("turtle")
colors = ["red", "purple"]
for color in colors:
    turtle.color(color)
    for i in range(num_sides):
         turtle.forward(length_sides)
         turtle.left(angle)
    window.exitonclick() 




#turtle.forward(length_side)
#turtle.left(angle)
