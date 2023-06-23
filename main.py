import turtle
from turtle import Turtle, Screen
from random import choice
import colorgram

#rgb_colors = []
#colors = colorgram.extract("image.jpg", 30)
#for color in colors:
 #   r = color.rgb.r
  #  g = color.rgb.g
   # b = color.rgb.b
    #new_colors = (r,g,b)

#    rgb_colors.append(new_colors)
#print(rgb_colors)
color_list = [(241, 233, 45), (195, 12, 35), (239, 41, 131), (224, 157, 67), (41, 83, 176), (44, 214, 69), (190, 71, 29), (33, 36, 157), (235, 228, 4), (73, 11, 46), (23, 148, 26), (199, 35, 81), (198, 15, 7), (230, 151, 9), (238, 56, 31), (56, 18, 11), (218, 135, 187), (71, 75, 218), (88, 210, 134), (82, 189, 221), (20, 16, 50), (240, 156, 209), (102, 232, 177), (14, 95, 63), (11, 210, 225), (90, 74, 13)]
tim = turtle.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.shape("arrow")
turtle.colormode(255)


def set_position(xcor, ycor):
    tim.penup()
    tim.goto(xcor,ycor)
    tim.penup()

def hisrt_painting():
    xcor = -250
    ycor = -250
    for y in range(10):
        set_position(xcor, ycor)
        for x in range(9):
            tim.dot(20, choice(color_list))
            tim.penup()
            tim.forward(50)
            tim.dot(20, choice(color_list))
        ycor += 50


hisrt_painting()

Screen = Screen()
Screen.exitonclick()