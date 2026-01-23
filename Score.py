from turtle import Turtle
class Score(Turtle):
    def __init__ (self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(0, 200)
        self.color("white")
        self.score = 0

    def add_point(self):
        self.score +=1
        return

    def show_score(self):
        self.write("Puntuación: " + str(self.score), False, "center", ("Arial", 18, "normal"))
        return

    def show_end_game(self):
        self.setposition(0,0)
        self.write("Game Over", False, "center", ("Arial", 18, "normal"))
        return





