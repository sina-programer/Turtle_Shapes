from turtle import Screen, Turtle
from itertools import cycle

class Shape:
    colors = iter(cycle(['red', 'purple', 'blue', 'green', 'orange', 'yellow']))
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        
    def draw(self):
        for time in range(510):
            self.turtle.color(next(self.colors))
            self.turtle.forward(time)
            self.turtle.right(59.7)
         

if __name__ == "__main__":
    root = Screen()
    root.bgcolor("black")
    root.title("Spiral Shape")
    
    shape = Shape()
    shape.draw()
    
    root.exitonclick()
