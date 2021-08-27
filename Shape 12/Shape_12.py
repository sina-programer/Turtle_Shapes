from turtle import Screen, Turtle

class Shape:
    def __init__(self, color, pen_size, x, y):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setpos(x=x , y=y)
        self.turtle.pendown()
        self.turtle.color(color)
        self.turtle.pensize(pen_size)
        self.turtle.speed(0)
        
    def draw(self, r, deg=10, times=36):
        for time in range(times):
            self.turtle.circle(r)
            self.turtle.left(deg)


if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')  
    root.title('Shape 12')
    root.setup(width=700, height=700)

    shape = Shape('blue', 2, 0, 30)
    shape.draw(100)
    
    root.exitonclick()
