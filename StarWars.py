import turtle


def balra():
    ship.setx(ship.xcor() - 30)


def jobbra():
    ship.setx(ship.xcor() + 30)


def fel():
    ship.sety(ship.ycor() + 30)


def le():
    ship.sety(ship.ycor() - 30)


def teleportx(amount):
    ship.hideturtle()
    ship.setx(amount)
    ship.showturtle()


def teleporty(amount):
    ship.hideturtle()
    ship.sety(amount)
    ship.showturtle()


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("src/space.png")
space.addshape("src/sprite.gif")
space.onkeypress(balra, "Left")
space.onkeypress(jobbra, "Right")
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")

ship = turtle.Turtle()
ship.shape("src/sprite.gif")
ship.penup()

while True:
    space.listen()
    if ship.xcor() >= 400:
        teleportx(-380)
    if ship.xcor() <= -400:
        teleportx(380)
    if ship.ycor() >= 300:
        teleporty(-280)
    if ship.ycor() <= -300:
        teleporty(280)
    space.update()
