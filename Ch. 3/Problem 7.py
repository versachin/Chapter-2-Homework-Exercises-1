pirate=[160, -43, 270, -97, -43, 200, -940, 17, -86]
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
Versachin=turtle.Turtle()
Versachin.shape("turtle")
for i in pirate:
    Versachin.right(i)
    Versachin.forward(100)
print(Versachin.heading())    
