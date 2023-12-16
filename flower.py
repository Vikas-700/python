import turtle

def draw_flower(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


    turtle.color("hotpink")
    turtle.begin_fill()
for i in range(21):
   for i in range(34):

    turtle.forward(10)

    turtle.left(200)
    turtle.end_fill()

    turtle.color("Yellow")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()


    turtle.speed(0)
draw_flower()
turtle.done()    


