from turtle import Turtle
class Score(Turtle):
    def __init__ (self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(0, 260)
        self.color("white")
        self.score = 0

    def add_point(self) -> None:
        """Add one point to the score."""
        self.score +=1
        return

    def show_score(self) -> None:
        """Show the actual score"""
        self.write("Puntuación: " + str(self.score), False, "center", ("Arial", 18, "normal"))
        return

    def show_end_game(self) -> None:
        """Show the message of the end of the game"""
        self.setposition(0,0)
        self.write("Game Over", False, "center", ("Arial", 18, "normal"))
        return





