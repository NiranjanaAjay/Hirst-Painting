# import colorgram
import turtle
from turtle import Turtle,Screen
import random
# colours=colorgram.extract("image.jpg.png",15)

timmy=Turtle()
turtle.colormode(255)
timmy.speed("fastest")
colour_list=[(245, 241, 231), (134, 84, 59), (194, 151, 95), (171, 142, 69), (70, 91, 104), (76, 96, 80), (112, 150, 162), (130, 164, 139), (193, 97, 72), (115, 44, 35), (149, 131, 143), (107, 148, 96), (224, 193, 137)]

timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
dot_count=100

for i in range(1,dot_count+1):
    timmy.dot(20,random.choice(colour_list))
    timmy.penup()
    timmy.forward(50)
    if i%10==0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


# for i in range (0,15):
#     r=colours[i].rgb.r
#     g = colours[i].rgb.g
#     b = colours[i].rgb.b
#     tup=(r,g,b)
#     list.append(tup)
# print(list)
screen=Screen()
screen.exitonclick()
