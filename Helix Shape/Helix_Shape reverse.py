from turtle import Screen, Turtle

class Shape:
    def __init__(self, color, pen_size, x, y):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setposition(x=x , y=y)
        self.turtle.pendown()
        self.turtle.color(color)
        self.turtle.pensize(pen_size)
        self.turtle.speed(0)
        
    def draw(self, times=320):
        for time in range(times):
            self.turtle.circle(times-time, extent=time-(time-30))


if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Helix Shape reverse')
    root.setup(width=700, height=700)

    shape = Shape('cyan', 4, 0, -300)
    shape.draw()
    
    root.exitonclick()
