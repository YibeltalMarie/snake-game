from turtle import Turtle,Screen
from snake_food import Food
screen = Screen()
ALIGNMENT = "center"
FONT = ("Arial",15,"normal")

class ScoreCounter(Turtle):
    def __init__(self):
        super().__init__()
        with open ("data.txt") as file:
            self.high_score = int(file.read())
        self.count_score = 0
        self.penup()
        self.color("white")
        self.goto(-50,270)
        self.screen_update()
        self.hideturtle()

    def screen_update(self):
        self.clear()
        self.write(f"score:{self.count_score}  high score :{self.high_score}",align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.count_score > self.high_score:
            self.high_score = self.count_score
            with open("data.txt",mode="w") as file:
                 file.write(f"{self.high_score}")
        self.count_score = 0
        self.screen_update()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def score_add(self):
        self.count_score += 1
        self.screen_update()





