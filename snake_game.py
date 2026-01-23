from turtle import Screen
from Snake import Snake
from Food import Food
from Score import Score
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
scoreboard = Score()

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
    scoreboard.clear()
    scoreboard.show_score()
    screen.update() # Refresh automatically the screen
    time.sleep(0.1)
    snake.move()

    #Detect the coalition with the food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    #Detect coalition with the vertical walls
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290:
        game_is_on = False

    # Detect coalition with the horizontal walls
    elif snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        game_is_on = False

    #Detect coalitions with the tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False

#Game over message
scoreboard.show_end_game()
screen.exitonclick()
print("GAME OVER")