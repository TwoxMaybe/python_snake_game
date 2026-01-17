from turtle import Turtle

# Constantes sugeridas para evitar "Magic Numbers"
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):

        # Atributo para almacenar los objetos Turtle (segmentos)
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """Itera sobre las posiciones iniciales para crear el cuerpo."""

        #Creamos los 3 primeros elementos de la serpiente
        for starting_pos in STARTING_POSITIONS:
            self.add_segment(starting_pos)

        return

    def add_segment(self, position):
        """Crea una nueva instancia de Turtle y la configura."""

        #Creamos el segmento
        segment = Turtle()

        #Lo configuramos
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.setposition(position)

        #Lo agregamos al cuerpo
        self.segments.append(segment)

        return

    def move(self):
        """Mueve la serpiente hacia adelante un paso."""
        last_segment_index = len(self.segments) - 1

        #Para mover el cuerpo
        for i in range(last_segment_index,0,-1):

            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].setposition(new_x,new_y)

        #Para mover la cabeza
        self.segments[0].forward(20)

        return

    def up(self):
        """Cambia la dirección de la cabeza hacia arriba."""

        #Evitar que choque la cabeza con su propio cuerpo
        if not (int(self.segments[0].heading()) == 270):
            self.segments[0].setheading(90)

        return

    def down(self):
        """Cambia la dirección de la cabeza hacia abajo."""

        # Evitar que choque la cabeza con su propio cuerpo
        if not (int(self.segments[0].heading()) == 90):
            self.segments[0].setheading(270)
        return

    def left(self):

        #Evitar que choque la cabeza con su propio cuerpo
        if not (int(self.segments[0].heading()) == 0):
            self.segments[0].setheading(180)

    def right(self):

        # Evitar que choque la cabeza con su propio cuerpo
        if not (int(self.segments[0].heading()) == 180):
            self.segments[0].setheading(0)

    def extend(self):
        """Añade un nuevo segmento a la serpiente."""
        self.add_segment(self.segments[-1].position())
        return
