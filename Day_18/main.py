import colorgram
import random
import turtle as t


def colours_palette(picture, n_colour):
    """It takes as parameters a picture (file jpg) and amount of the colours you want to get
       It returns a list with the tuple with the numbers r, g, b"""
    colors = colorgram.extract(picture, n_colour)
    colors_rgb = []
    for item in colors:
        r = item.rgb[0]
        g = item.rgb[1]
        b = item.rgb[2]
        colors_rgb.append((r, g, b))
    return colors_rgb


tim = t.Turtle()
t.colormode(255)
tim.hideturtle()
Hirst_palette = colours_palette('images.jpg', n_colour=88)
tim.penup()
tim.goto(-300, -225)
lines = 0
while lines < 10:
    for _ in range(10):
        tim.pendown()
        colour = random.choice(Hirst_palette)
        tim.dot(20, colour)
        tim.penup()
        tim.forward(50)
    lines += 1
    tim.penup()
    tim.goto(-300, (50 * lines) - 225)


screen = t.Screen()
screen.exitonclick()
