"""num=int(input("Enter any number:"))
sum_of_all=0
lenth=str(num)
whirth=len(lenth)
sum_of_all=sum(int(digit)**whirth for digit in lenth)  
if sum_of_all==num:
    print("Armstrong Number.")
else:
    print("It is not a armstrong numaber.")"""
import turtle
t=turtle.Turtle()
t.pencolor("RED")
t.speed(0)
t.pensize(2)
for i in range(50,550):
    t.begin_fill()
    t.fillcolor("RED")
    if i<100:
        t.pencolor("GREEN")
    elif i<130 and i>100:
        t.pencolor("YELLOW")
    elif i<170 and i>130:
        t.pencolor("BROWN")  
    else:
        t.pencolor("BLUE")          
    t.circle(i)
    t.backward(4)
    t.right(5)
    t.end_fill()   