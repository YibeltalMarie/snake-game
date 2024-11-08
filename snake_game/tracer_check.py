import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Using tracer() and update() with time")

# Turn off automatic updates
screen.tracer(0)

# Create a turtle instance
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

t.goto(-200, 0)
t.forward(100)


# Move the turtle with controlled timing
for _ in range(100):
    t.forward(4)
    t.penup()
    screen.update()  # Manually update the screen
    time.sleep(0.05)  # Pause for 50 milliseconds

turtle.done()
