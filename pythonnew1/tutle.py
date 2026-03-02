"""import turtle
color=["red","purple","blue","green","orange","yellow"]
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.speed(0)
    t.pencolor(color[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)"""

"""from turtle import*
color('red')
#fillcolor()
while True:
    speed(0)
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()"""

"""import turtle
screen=turtle.Screen()
screen.title("click the Turtle")
my_turtle=turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")
my_turtle.penup()

def moveto(x,y):
    my_turtle.goto(x,y)
    print(f"Turtle moved to:({x},{y})")
my_turtle.onclick(moveto)
screen.mainloop()"""

"""from turtle import *
color("red")
fillcolor('yellow')
begin_fill()
while True:
    speed(1)
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()"""



"""import turtle
loadWindow=turtle.Screen()
turtle.speed(0)
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()"""

from turtle import*
forward(200)
up()
forward(100)
down()
forward(50)
done()

