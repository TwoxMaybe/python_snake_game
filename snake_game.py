from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
import time

#Screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0) #Off automatic animations

#Objects creation
snake = Snake()
food = Food()

# Controls keys configurations
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

#Control variable
game_is_on = True

#Principal loop
while game_is_on:
    screen.update() # Refresh automatically the screen
    time.sleep(0.1)
    snake.move()

    #Detect the coalition with the food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()

    #Detect coalition with the vertical walls
    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300:
        game_is_on = False
        print("GAME OVER")

    # Detect coalition with the horizontal walls
    elif snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
        game_is_on = False
        print("GAME OVER")

    #Detect coalitions with the tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            print("GAME OVER")