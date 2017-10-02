import turtle
wn = turtle.Screen()
grotto = turtle.Turtle()
grotto.color("blue")
grotto.pensize(3)
wn.bgcolor("lightgreen")
grotto.shape("turtle")

grotto.stamp()
for i in range(12):
    grotto.penup()
    grotto.forward(150)
    grotto.pendown()
    grotto.forward(20)
    grotto.stamp()
    grotto.penup()
    grotto.setpos(0, 0)
    grotto.left(360/12)

grotto.hideturtle()
    
