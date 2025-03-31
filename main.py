import turtle
from turtle import Turtle, Screen
import time
from Snake import Snake
from food import Food
from scoreboard import scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
turtle.tracer(0)

snake = Snake()
food = Food()
score = scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True


while is_game_on:
    turtle.update()
    time.sleep(0.1)
    snake.move()

    # Detects collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detects collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        is_game_on = False
        score.gameover()

    # Detects collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.gameover()




screen.exitonclick()
