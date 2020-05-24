import turtle

window = turtle.Screen()
alex = turtle.Turtle()

def goforward():
    alex.forward(150)
def turnleft():
    alex.left(90)
def turnright():
    alex.right(90)
def byebye():
    window.bye
def jump(x, y):
    alex.goto(x, y)
window.onkey(goforward, "Up")
window.onkey(turnleft, "Left")
window.onkey(turnright, "Right")
window.onkey(byebye, "Escape")

window.onclick(jump)

window.listen()
window.mainloop()