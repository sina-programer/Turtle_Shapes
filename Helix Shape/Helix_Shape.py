from turtle import Screen, Turtle

class Shape:
    def __init__(self, color, pen_size):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.color(color)
        self.turtle.pensize(pen_size)
        self.turtle.speed(0)
        
    def draw(self, times=650):
        for time in range(times):
            self.turtle.circle(time*.5, extent=time-(time-15))


if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Helix Shape')
    root.setup(width=700, height=700)

    shape = Shape('cyan', 4)
    shape.draw()
    
    root.exitonclick()
