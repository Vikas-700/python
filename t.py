import turtle
t=turtle.Turtle()
sc=turtle.Screen()
sc.bgcolor("black")
t.speed(3)
t.pencolor("white")
for i in range(1,10):
    t.pencolor("yellow")
    t.up()
    t.goto(-10,20)
    t.down()
    t.begin_fill()
    t.fillcolor("yellow")
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.end_fill()