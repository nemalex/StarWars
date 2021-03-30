import turtle
import random
import winsound


def meteorjobbbal():
    meteor.setx(meteor.xcor() - 5)


def randommeteor():
    meteor.hideturtle()
    meteor.sety(random.randrange(-280, 280))
    meteor.setx(400)
    meteor.showturtle()


def balra():
    ship.setx(ship.xcor() - 30)


def jobbra():
    ship.setx(ship.xcor() + 30)


def fel():
    ship.sety(ship.ycor() + 30)


def le():
    ship.sety(ship.ycor() - 30)


def teleportx(xamount, yamount):
    ship.hideturtle()
    ship.setx(xamount)
    ship.sety(random.randrange(-yamount, yamount))
    ship.showturtle()


def teleporty(yamount, xamount):
    ship.hideturtle()
    ship.sety(yamount)
    ship.setx(random.randrange(-xamount, xamount))
    ship.showturtle()


def kijelzo_write(points):
    kijelzo.clear()
    kijelzo.write(f"{points}", align="center", font=("Arial", 36, "bold"))


def healt_write(healthpoints):
    health.clear()
    health.write(f"{healthpoints}", align="left", font=("Arial", 36, "bold"))


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("src/space.png")
space.addshape("src/sprite.gif")
space.addshape("src/meteor2.gif")
space.onkeypress(balra, "Left")
space.onkeypress(jobbra, "Right")
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")

meteor = turtle.Turtle()
meteor.shape("src/meteor2.gif")
meteor.hideturtle()
meteor.setposition(400, 20)
meteor.showturtle()
meteor.penup()

kijelzo = turtle.Turtle()
kijelzo.color("white")
kijelzo.hideturtle()
kijelzo.penup()
kijelzo.clear()
kijelzo.sety(240)

health = turtle.Turtle()
health.color("white")
health.hideturtle()
health.penup()
health.clear()
health.sety(240)
health.setx(350)

ship = turtle.Turtle()
ship.shape("src/sprite.gif")
ship.penup()

points = 0
kijelzo.write(f"{points}", align="center", font=("Arial", 36, "bold"))

healthpoints = 3
health.write(f"{healthpoints}", align="left", font=("Arial", 36, "bold"))

while True:
    space.listen()
    meteorjobbbal()
    if meteor.xcor() < -450:
        randommeteor()
        points += 1
        kijelzo_write(points)

    if ship.xcor() >= 400:
        teleportx(-380, 280)
    if ship.xcor() <= -400:
        teleportx(380, 280)
    if ship.ycor() >= 300:
        teleporty(-280, 380)
    if ship.ycor() <= -300:
        teleporty(280, 380)

    if ship.distance(meteor.xcor(), meteor.ycor()) < 15:
        randommeteor()
        healthpoints -= 1
        winsound.PlaySound("src/explosion-01.wav", 1)
        healt_write(healthpoints)

    if healthpoints == 0:
        kijelzo.clear()
        kijelzo.write("Game Over", align="center", font=("Arial", 36, "bold"))
        turtle.done()

    space.update()
