import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid= 1, stretch_len=1)
        self.color("blue")
        self.refresh()

    def refresh(self):

        """Moves randomly the food to a new position"""
        new_x = random.randint(-300,300)
        new_y = random.randint(-300,300)
        self.setposition(new_x,new_y)

        return
