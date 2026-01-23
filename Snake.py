from turtle import Turtle

#Directions based in the global angle of reference used for Turtle
Up = 90
Down = 270
Left = 180
Right = 0

class Snake:
    def __init__(self) -> None:
        self.segments = [] #Segments that compose the body of the snake (The first one is the head)
        self.create_snake()

    def create_snake(self) -> None:
        """"
        Create the initial body of the snake (head and 2 segments of body)
        """
        #Create and save the head
        self.add_segment((0,0))

        #For the body make the same but his position have to be behind the head
        #We create 2 segments more to the initial Snake
        for i in range(0, 2):
            self.add_segment((i * -20, 0))
        return

    def add_segment(self, position: tuple[int, int]) -> None:
        """Create the segment and configurate his 
        appearance to append it to the body of the snake."""

        #We create the object turtle
        segment = Turtle()

        #We configure his appearances
        segment.shape("square")
        segment.color("white")
        segment.penup() # We don't want to draw the followed path
        segment.setposition(position)

        #We append it to the body
        self.segments.append(segment)

        return

    def move(self) -> None:
        """Makes the automatic movement of the snake.
        The logic is: The body follows the head, if one part of the body moves
        the segment behind it takes his place"""

        last_segment_index = len(self.segments) - 1

        #We go from the tail to the head
        for i in range(last_segment_index,0,-1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].setposition(new_x,new_y)

        #After all the movement of the body we move the head
        self.segments[0].forward(20)

        return

    def up(self) -> None:
        """Changes the direction of the snake to the up."""

        #Avoid the crash of the head with the body (he can't turn 180 degrees )
        if not (int(self.segments[0].heading()) == Down):
            self.segments[0].setheading(90)
        return

    def down(self) -> None:
        """Changes the direction of the snake to down."""

        #Avoid the crash of the head with the body (he can't turn 180 degrees )
        if not (int(self.segments[0].heading()) == Up):
            self.segments[0].setheading(270)
        return

    def left(self) -> None:
        """Changes the direction of the snake to the left."""

        ##Avoid the crash of the head with the body (he can't turn 180 degrees)
        if not (int(self.segments[0].heading()) == 0):
            self.segments[0].setheading(180)
        return

    def right(self) -> None:
        """Changes the direction of the snake to the right."""

        #Avoid the crash of the head with the body (he can't turn 180 degrees )
        if not (int(self.segments[0].heading()) == Left):
            self.segments[0].setheading(0)

        return

    def extend(self) -> None:
        """Appends a new segment to the body"""
        self.add_segment(self.segments[-1].position())
        return
