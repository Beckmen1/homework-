from turtle import *




speed(5)
width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing door

forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
right(90)
forward(60)
left(90)

penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200,140)
right(90)
pendown()

left(30)
penup()
forward(20)
pendown()
forward(40)
right(90)
forward(54)
right(90)
forward(40)
right(90)
forward(50)

right(90)
penup()
forward(120)
pendown()
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(52)

exitonclick()