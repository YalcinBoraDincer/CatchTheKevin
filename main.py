import random
import turtle

# Screen
wn = turtle.Screen()
wn.bgcolor('#EEE8AA')
wn.title('CatchTheKevin')
wn.setup(1000, 800)

# Image
image = "kevin.gif"
wn.addshape(image)
wn.listen()

# Skor
score = 0

# Countdown Turtle
countdown_turtle = turtle.Turtle()
countdown_turtle.hideturtle()
countdown_turtle.penup()
countdown_turtle.color("dark blue")
countdown_turtle.goto(0, 300)

# Skor Turtle
score_turtle = turtle.Turtle()
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.color("purple")
score_turtle.goto(0, 350)

# Image Turtle
image_turtle = turtle.Turtle()
image_turtle.shape(image)
image_turtle.penup()
image_turtle.hideturtle()

# Score
def update_score(x, y):
    global score
    score += 1
    scoreBoard()

# Random Coordinate
def randomCoordinate():
    x = random.randrange(-450, 450)
    y = random.randrange(-350, 300)
    image_turtle.goto(x, y)

# Scoreboard
def scoreBoard():
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align='center', font=("Comic Sans MS", 25, "bold"))

# Countdown
def countDown(time_left):
    if time_left >= 0:
        countdown_turtle.clear()
        countdown_turtle.write(f"Time: {time_left}", align='center', font=("Comic Sans MS", 25, "bold"))
        randomCoordinate()
        image_turtle.showturtle()
        image_turtle.onclick(update_score)

        wn.ontimer(lambda: image_turtle.hideturtle(), 500)
        wn.ontimer(lambda: countDown(time_left - 1), 1000)
    else:
        countdown_turtle.clear()
        countdown_turtle.write(f"Time's up! Final Score: {score}", align='center', font=("Comic Sans MS", 25, "bold"))


scoreBoard()
countDown(30)


turtle.mainloop()
