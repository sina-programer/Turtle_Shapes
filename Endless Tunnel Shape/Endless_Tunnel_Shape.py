from turtle import Screen, Turtle

class Shape:
    def __init__(self, color):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.color(color)
        self.turtle.speed(0)
        
    def draw(self, times=600):
        for time in range(times):
            self.turtle.forward(time)
            self.turtle.right(90)


if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Endless Tunnel Shape')
    root.setup(width=600, height=600)
    
    shape = Shape('white')
    shape.draw()

    root.exitonclick()
