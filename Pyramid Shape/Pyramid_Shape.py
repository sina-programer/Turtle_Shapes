from turtle import Screen, Turtle

class Shape:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.color()
        self.turtle.speed(0)
        
    def draw(self, deg=120, times=500):
        for time in range(times):
            self.turtle.forward(time)
            self.turtle.left(deg)


if __name__ == "__main__":
    root = Screen()
    root.title('Pyramid Shape')
    
    shape = Shape()
    shape.draw()

    root.exitonclick()
