
from score_counter import ScoreCounter
ALIGNMENT = "center"
FONT = ("Arial",15,"normal")

class Highscore(ScoreCounter):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.goto(100,270)
        self.high_score_updater()

    def high_score_updater(self):
        self.clear()
        self.write(f"high score :{self.high_score}", align=ALIGNMENT, font=FONT)

    def high_score_checker(self):
        if self.count_score <= self.high_score:
            self.high_score_updater()

        else:
            self.high_score = self.count_score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
            self.high_score_updater()