from turtle import Screen
from snake1 import Snake
from snake_food import Food
from score_counter import ScoreCounter
# from highscoreupdater import Highscore
import time
screen = Screen()
screen.setup(600,600)
screen.title("this is my snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

score = ScoreCounter()

food = Food()

# highscore = Highscore()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
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
        # highscore.high_score = score.count_score
        # game_is_on = False
        # # highscore.high_score_checker()
        # score.game_over()
        score.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            # highscore.high_score = score.count_score
            # highscore.high_score_checker()
            # game_is_on = False
            # score.game_over()
            score.reset()
            snake.reset()
# def want_continue ():
#     user_choice = screen.textinput("GAME OVER","do you play again?(yes/no)")
#     if user_choice == "yes":
#         return True
#     else:
#         return False
#
# while True:
#     snake_loop()
#     if want_continue():
#         # snake.count_score = 0
#         # score.screen_update()
#         snake_loop()
#     else:
#         score.game_over()
#         break



screen.exitonclick()