import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
ablak.title("Teknocok")

Sanyi = turtle.Turtle()
Sanyi.color("blue")
Sanyi.pensize(4)
Sanyi.forward(50)
Sanyi.penup()
Sanyi.forward(50)
Sanyi.pendown()
Sanyi.left(90)
Sanyi.forward(100)

Mari = turtle.Turtle()
Mari.color("red")
Mari.pensize(2)
Mari.speed(1)
Mari.right(315)
Mari.forward(100*2**0.5)

ablak.mainloop()