from turtle import Screen, Turtle

class Shape:
    def __init__(self, color):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.color(color)
        self.turtle.pensize(4)
        self.turtle.speed(0)
        
    def draw(self, times=200):
        for time in range(times):
            self.turtle.circle(100-time)


if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Circle Shape')
    
    shape = Shape('cyan')
    shape.draw()

    root.exitonclick()
