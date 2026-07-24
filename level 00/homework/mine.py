from turtle import *
# i want to draw house
# first make square
speed(20)

shape("turtle")
width(5)
color("dark red")
forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90)

#i maked square then i will make door
begin_fill()
forward(100)

color("yellow")

left(90)
forward(180)
right(90)
forward(100)
right(90)
forward(180)

end_fill()


# make roof
penup()
goto(300,300)
pendown()
color("yellow")

begin_fill()
right(130)
forward(200)

left(80)
forward(200)
end_fill()

# first window
penup()
goto(100,260)
pendown()

color("blue")
right(40)
forward(80)
left(90)
forward(60)
left(90)

forward(80)
left(90)
forward(60)

left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(80)

# second window
penup()
goto(280,260)
pendown()

color("blue")


forward(80)
left(90)
forward(60)
left(90)

forward(80)
left(90)
forward(60)

left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(80)

# make garden
penup()
goto(00,00)
pendown()

color("green")
begin_fill()
forward(500)
left(90)

forward(500)
left(90)

forward(1300)
left(90)

forward(500)
left(90)

forward(500)
end_fill()

left(180)
forward(500)
right(90)
forward(180)
right(90)
begin_fill()
color("grey")


forward(1300)

left(90)

forward(140)

left(90)

forward(1300)
left(90)
forward(140)

left(90)
forward(600)
right(90)
forward(180)
left(90)
forward(100)
left(90)
forward(180)
end_fill()


exitonclick()