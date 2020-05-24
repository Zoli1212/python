import turtle
import math



window =turtle.Screen()
teki = turtle.Turtle()

teki.forward(30)
teki.left(90)
teki.forward(40)
teki.left(180-(math.atan2(30, 40)/3.14*180))

teki.forward(50)
window.mainloop()