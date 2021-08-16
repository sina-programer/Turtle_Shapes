from turtle import Screen, Turtle

class Shape:
    def __init__(self, size, color, x, y, speed=10):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setposition(x=x , y=y)
        self.turtle.pendown()
        self.turtle.color(color)
        self.turtle.pensize(size)
        self.turtle.speed(speed)
        
    def draw(self, times=45):
        for time in range(times):
            self.turtle.circle(500, extent=50)
            self.turtle.circle(20, extent=130)
            self.turtle.left(4)


if __name__ == "__main__":
    win = Screen()
    win.bgcolor("black")
    win.title("Shape 8")
    win.setup(width=600 , height=600 , startx=400 , starty=130)
    
    shape = Shape(3, 'blue', -190, -90)
    shape.draw()
    
    win.exitonclick()

