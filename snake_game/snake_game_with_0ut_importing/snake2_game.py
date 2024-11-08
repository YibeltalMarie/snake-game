from turtle import Turtle,Screen
import random
import time
screen = Screen()
screen.setup(600,600)
screen.title("this is my snake game")
screen.bgcolor("black")
screen.tracer(0)

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake :

    def __init__(self):
        self.segments = []
        self.length = -40
        self.creating_snake()

    # I REALLY WANT TO RAISE A QUESTION HERE
    def creating_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for new_seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[new_seg - 1].xcor()
            new_y = self.segments[new_seg - 1].ycor()
            self.segments[new_seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    # I REALLY WANT TO RAISE A QUESTION HERE
    def add_segments(self):
        self.length -= -20
        position = (self.length,0)
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.move()


    def up(self):
        if self.segments[0].heading() != DOWN :
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP :
            self.segments[0].setheading(DOWN)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

snake = Snake()

from turtle import Turtle,Screen

screen = Screen()
ALIGNMENT = "center"
FONT = ("Arial",15,"normal")

class ScoreCounter(Turtle):
    def __init__(self):
        super().__init__()
        self.count_score = 0
        self.penup()
        self.color("white")
        self.text = "score : "
        self.goto(0,270)
        self.screen_update()
        self.hideturtle()

    def screen_update(self):
        self.write(self.text+ str(self.count_score),align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def score_add(self):
        self.clear()
        self.count_score += 1
        self.screen_update()
score = ScoreCounter()


class Food(Turtle) :
    colors = ["red", "yellow", "green", "blue", "purple", "brown"]
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(self.colors))
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        self.color(random.choice(self.colors))
        random_x = random.randint(-290, 290)
        random_y = random.randint(-290, 290)
        self.goto(random_x,random_y)

food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on :
    screen.update()
    time.sleep(.1)
    snake.move()

    # to add score up  and get food as soon as it is eaten
    if snake.segments[0].distance(food) < 15:
        snake.add_segments()
        score.score_add()
        food.refresh()


    # to detect when the snake crash with wall
    if snake.segments[0].xcor()>299 or snake.segments[0].xcor()<-300 or snake.segments[0].ycor()>300 or snake.segments[0].ycor()<-299:
        game_is_on = False
        score.game_over()