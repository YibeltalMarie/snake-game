
from turtle import Turtle
from snake_food import Food
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
            self.add_segments(position)

    # I REALLY WANT TO RAISE A QUESTION HERE
    def add_segments(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # I REALLY WANT TO RAISE A QUESTION HERE
    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move (self):
        for new_seg in range (len(self.segments)-1, 0, -1):
            new_x = self.segments[new_seg-1].xcor()
            new_y = self.segments[new_seg - 1].ycor()
            self.segments[new_seg].goto(new_x,new_y)
        self.segments[0].forward(20)



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















