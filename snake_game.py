from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
import time

# --- Configuración Global ---

#Configuración de la pantalla
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0) #Para apagar las animaciones automaticas

#Configuración de los objetos
snake = Snake()
food = Food()

# Configuración de las teclas
screen.listen() # Habilita la ventana para recibir señales
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")


#Variables de control
game_is_on = True

#Bucle principal
while game_is_on:
    screen.update() # Refresca la pantalla manualmente
    time.sleep(0.1)
    snake.move()

# 1. Detectar colisión con comida
    if snake.segments[0].distance(food) < 15:
        pass # ¿Qué pasa aquí? (Mover comida, extender serpiente)
        food.refresh()
        snake.extend()

    # 2. Detectar colisión con pared
    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300:
        game_is_on = False
        print("GAME OVER")

    elif snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
        game_is_on = False
        print("GAME OVER")

    # 3. Detectar colisión con la cola
    # Pista: Hay que iterar sobre los segmentos (menos la cabeza)
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            print("GAME OVER")